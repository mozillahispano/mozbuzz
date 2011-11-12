from django.shortcuts import render

from mozbuzz.buzz.constants import INDEX_TEMPLATE
from mozbuzz.buzz.models import Mention, FEEDBACK_TYPES, UPDATE_RATE
import mozbuzz.buzz.search as search

def index(request):
    """Display Home page."""
    data = {}

    data['mentions'] = search.buzz_search(request.GET)
    data['FEEDBACK_TYPES'] = FEEDBACK_TYPES
    data['UPDATE_RATE'] = UPDATE_RATE
    data['query'] = search.clean_query(request.GET)

    return render(request, INDEX_TEMPLATE, data)


def about(request):
    pass #TODO
