from django.shortcuts import render

from mozbuzz.buzz.constants import INDEX_TEMPLATE
from mozbuzz.buzz.models import Mention

def index(request):
    """Display Home page."""
    data = {}

    data['mentions'] = Mention.enabled.all()

    return render(request, INDEX_TEMPLATE, data)


def about(request):
    pass #TODO
