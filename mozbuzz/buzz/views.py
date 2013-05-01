import urllib, feedparser, time, datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
import django.utils.functional as functional
from django.conf import settings

from mozbuzz.buzz.forms import MentionForm, FollowUpForm
from mozbuzz.buzz.models import Mention, FollowUp, RSSPost, RSSFeed, Product
from mozbuzz.buzz.search import buzz_search, clean_query
from mozbuzz.buzz.utils import mozview, jsonview

login_required = functional.curry(login_required, login_url="/" + settings.URL_PREFIX + "accounts/login/")


@login_required
@mozview
def index(request):
    """Display Home page."""
    query = clean_query(request.GET)
    return {
        "query": query,
        "mentions": buzz_search(query)
    }

@login_required
@mozview
def mention_view(request, pk):
    return {
        "mention": get_object_or_404(Mention, pk=pk)
    }

def about(request):
    pass #TODO


@login_required
@mozview
def mention(request, pk=None):
    is_new = False
    if request.method == 'POST':
        if pk is None:
            instance = Mention(creation_user=request.user)
        else:
            instance = Mention.enabled.get(pk=pk)
        form = MentionForm(request.POST, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.last_update_user = request.user
            instance.save()

            if "rsspost_hide" in request.POST:
                RSSPost.objects.filter(pk=int(request.POST["rsspost_hide"])).delete()

            return HttpResponseRedirect(reverse(index))
    elif pk is not None:
        form = MentionForm(instance=Mention.enabled.get(pk=pk))
    else:
        is_new = True
        form = MentionForm(initial={
            "link": request.GET.get("url","http://")
        })

    return {"form": form, "pk": pk, "is_new": is_new}


@login_required
@mozview
def followup(request, pk=None, mention=None):
    if pk is None:
        #create new
        mention = get_object_or_404(Mention, pk=mention)
        instance = FollowUp(creation_user=request.user, mention=mention)
    else:
        #edit existing
        instance = get_object_or_404(FollowUp, pk=pk)
        assert instance.creation_user == request.user

    if request.method == 'POST':
        form = FollowUpForm(request.POST, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.last_update_user = request.user
            instance.save()
            return HttpResponseRedirect(reverse(index))
    else:
        form = FollowUpForm(instance=instance)

    return {"form": form}


@login_required
def proxy(request):
    assert "url" in request.GET
    return HttpResponse(urllib.urlopen(request.GET["url"]).read())


@login_required
@jsonview
def source_json(request,source):
    return [x.__obj__() for x in Mention.objects.filter(source_name=source)]


@login_required
@mozview
def queue(request,product=None):
    posts = RSSPost.objects.filter(hidden=False)

    if product is not None:
        product = get_object_or_404(Product,slug=product)
        posts = posts.filter(feed__product=product)

    return {
        "posts": posts.order_by("pub_date").select_related("feed"),
        "product": product,
    }


@login_required
@mozview
def update_queue(request):
    for feed in RSSFeed.objects.all():
        result = feedparser.parse(feed.url)
        for entry in result.entries:
            try:
                entryObj = feed.posts.get(guid=entry.guid)
            except RSSPost.DoesNotExist:
                entryObj = RSSPost(guid=entry.guid, feed=feed)

            entryObj.title = entry.title
            entryObj.link = entry.link
            entryObj.pub_date = datetime.datetime(*entry.updated_parsed[0:6])
            entryObj.description = entry.summary
            entryObj.save()

    return HttpResponseRedirect(reverse(queue))


@login_required
@jsonview
def queue_del(request):
    post = RSSPost.objects.get(pk=request.POST["post"])
    post.hidden = True
    post.save()
    return {
        "queue_count": RSSPost.objects.filter(hidden=False).count()
    }

