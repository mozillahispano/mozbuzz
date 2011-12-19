from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from mozbuzz.buzz.forms import MentionForm, FollowUpForm
from mozbuzz.buzz.models import Mention, FollowUp
from mozbuzz.buzz.search import buzz_search, clean_query
from mozbuzz.buzz.utils import mozview

@mozview
def index(request):
    """Display Home page."""
    query = clean_query(request.GET)
    return {
        "query": query,
        "mentions": buzz_search(query)
    }

def about(request):
    pass #TODO

@login_required
@mozview
def mention(request, pk=None):
    if request.method == 'POST':
        if pk is None:
            instance = Mention(creation_user=request.user)
        else:
            instance = Mention.enabled.get(pk=pk)
        form = MentionForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    elif pk is not None:
        form = MentionForm(instance=Mention.enabled.get(pk=pk))
    else:
        form = MentionForm()

    return {"form": form, "pk": pk}

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
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = FollowUpForm(instance=instance)

    return {"form": form}
