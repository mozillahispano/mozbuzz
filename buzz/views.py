from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from mozbuzz.buzz.constants import TEMPLATE_INDEX, TEMPLATE_CREATE, TEMPLATE_FOLLOWUP
from mozbuzz.buzz.forms import MentionForm, FollowUpForm
from mozbuzz.buzz.models import Mention, FollowUp, FEEDBACK_TYPES, UPDATE_RATE
from mozbuzz.buzz.search import buzz_search, clean_query

def get_base_data(request):
    data = {}
    data['FEEDBACK_TYPES'] = FEEDBACK_TYPES
    data['UPDATE_RATE'] = UPDATE_RATE
    query = clean_query(request.GET)
    data['query'] = query

    return data

def index(request):
    """Display Home page."""
    data = get_base_data(request)
    data['mentions'] = buzz_search(data['query'])

    return render(request, TEMPLATE_INDEX, data)


def about(request):
    pass #TODO

@login_required
def create(request):
    data = get_base_data(request)
    if request.method == 'POST':
        instance = Mention(creation_user=request.user)
        form = MentionForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = MentionForm()

    data['form'] = form

    return render(request, TEMPLATE_CREATE, data)


@login_required
def followup(request,pk=None,mention=None):
    data = get_base_data(request)

    if pk is None:
        #create new
        mention = get_object_or_404(FollowUp,pk=mention)
        instance = FollowUp(creation_user=request.user,mention=mention)
    else:
        #edit existing
        instance = get_object_or_404(FollowUp,pk=pk)
        assert instance.creation_user == request.user

    if request.method == 'POST':
        form = FollowUpForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = FollowUpForm(instance=instance)

    data['form'] = form

    return render(request, TEMPLATE_FOLLOWUP, data)
