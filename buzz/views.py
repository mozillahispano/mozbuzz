from django.shortcuts import render

def index(request):
    """Display Home page."""
    return render(request,"index.html",{})


def about(request):
    pass #TODO
