from mozbuzz.buzz.models import Mention

VALID_PARMS = {
    "feedback_type":"set",
    "update_rate":"set",
    "q":"str"
}

def buzz_search(query):
    objs = Mention.enabled.all()
    print query

    filters = {
        "feedback_type": lambda objs,val:objs.filter(feedback__in=val),
        "update_rate": lambda objs,val:objs.filter(update_rate__in=val),
        "q":lambda objs,val:objs.filter(text__contains=word)
    }

    for key,val in query.iteritems():
        type=VALID_PARMS[key]

        if type=="set" and len(val):
            objs = filters[key](objs,val)
        elif type=="str":
            keywords = val.split()
            for word in keywords:
                objs = filters[key](objs,word)

    return objs


def clean_query(query):
    res = {}
    for parm,type in VALID_PARMS.iteritems():
        if parm in query and len(query[parm]):
            if type=="set":
                res[parm] = set(map(int,query[parm].split(",")))
            elif type=="str":
                res[parm] = query[parm]
        elif type=="set":
            res[parm] = set(())

    return res

