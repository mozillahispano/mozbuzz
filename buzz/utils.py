from mozbuzz.buzz.models import FEEDBACK_TYPES, UPDATE_RATE, Country,
Product, MentionType, AuthorExpertise, Source, RSSPost
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse, Http404
import json


def queue_context_processor(request):
    return {
        "queue_count": lambda: RSSPost.objects.filter(hidden=False).count(),
    }


def mozview(view):
    view_name = view.__name__

    def __inner__(request, *args, **kwargs):

        result = view(request, *args, **kwargs)
        if isinstance(result, HttpResponse):
            return result
        else:
            ctx = {
                "view_name": view_name,
                "FEEDBACK_TYPES": FEEDBACK_TYPES,
                "UPDATE_RATE": UPDATE_RATE,
                "COUNTRIES":
                lambda: dict([(c.pk, c.name) for c in Country.objects.all()]),
                "PRODUCTS":
                lambda: dict([(c.pk, c.name) for c in Product.enabled.all()]),
                "MENTION_TYPES":
                lambda:
                dict([(c.pk, c.name) for c in MentionType.enabled.all()]),
                "AUTHOR_EXPERTISES":
                lambda:
                dict([(c.pk, c.name) for c in AuthorExpertise.enabled.all()]),
                "MENTION_ORIGINS":
                lambda: dict([(c.pk, c.name) for c in Source.enabled.all()]),
            }
            ctx.update(result)
            return render(request, "%s.html" % view_name,
                          context_instance=RequestContext(request, ctx))

    return __inner__


def jsonview(view):

    def __inner__(*args, **kwargs):
        try:
            res = (200, view(*args, **kwargs))
        except Http404, e:
            res = (404, str(e))
        except Exception, e:
            res = (500, str(e))

        code, data = res

        httpres = HttpResponse(json.dumps({
            "status": code,
            "response": data,
        }), mimetype="application/json", status=code)

        httpres['Cache-Control'] = 'no-cache'

        return httpres

    return __inner__
