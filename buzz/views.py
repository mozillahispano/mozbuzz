from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from mozbuzz.buzz.constants import TEMPLATE_INDEX, TEMPLATE_CREATE
from mozbuzz.buzz.models import Mention, FEEDBACK_TYPES, UPDATE_RATE
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
    
    
    return render(request, TEMPLATE_CREATE, data)
