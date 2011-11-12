from mozbuzz.buzz.models import Mention

VALID_PARMS = (
    "feedback_type",
    "update_rate",
    "q"
)

def buzz_search(query):
    objs = Mention.objects.all()
    print query

    for key,val in query.iteritems():
        print key
        if key == "feedback_type":
            objs = objs.filter(feedback=int(val))
        elif key == "update_rate":
            objs = objs.filter(update_rate=int(val))
        elif key == "q":
            keywords = val.split()
            for word in keywords:
                objs = objs.filter(text__contains=word)

    return objs


def clean_query(query):
    res = {}
    for parm in VALID_PARMS:
        if parm in query:
            res[parm] = query[parm]

    return res

