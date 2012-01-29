from mozbuzz.buzz.models import Mention

VALID_PARMS = {
    "feedback_type":"set",
    "update_rate":"set",
    "q":"str",
    "audience_gt":"int",
    "audience_lt":"int",
}

DEFAULTS = {
    "feedback_type": set(()),
    "update_rate": set(()),
    "audience_gt": 0,
    "audience_lt": 7000000000,
}

def buzz_search(query):
    objs = Mention.enabled.all().order_by('-creation_date')
    print query

    filters = {
        "feedback_type": lambda objs,val:objs.filter(feedback__in=val),
        "update_rate": lambda objs,val:objs.filter(update_rate__in=val),
        "q":lambda objs,val:objs.filter(text__contains=word),
        "audience_gt": lambda objs, val: objs.filter(estimated_audience__gte=val),
        "audience_lt": lambda objs, val: objs.filter(estimated_audience__lte=val),
    }

    for key,val in query.iteritems():
        type=VALID_PARMS[key]

        if (type=="set" and len(val)) or type=="int":
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
            elif type=="int":
                res[parm] = int(query[parm])

        elif parm in DEFAULTS:
            res[parm] = DEFAULTS[parm]

    return res

