from mozbuzz.buzz.models import FEEDBACK_TYPES, UPDATE_RATE
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse

def mozview(view):
    view_name = view.__name__
    def __inner__(request, *args, **kwargs):

        result=view(request, *args, **kwargs)
        if isinstance(result,HttpResponse):
            return result
        else:
            ctx = {
                "view_name": view_name,
                "FEEDBACK_TYPES": FEEDBACK_TYPES,
                "UPDATE_RATE": UPDATE_RATE
            }
            ctx.update(result)
            return render(request, "%s.html" % view_name, context_instance=RequestContext(request, ctx))

    return __inner__

