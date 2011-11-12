from django import template
import urllib
register = template.Library()

def update_query(key):
    def __inner__(obj,val):
        obj = obj.copy()
        obj[key] = val
        return obj
    return __inner__

def encode_query(obj):
    return urllib.urlencode(obj)

def query_equals(obj,val):
    return obj == str(val)

register.filter("update_feedback",update_query("feedback_type"))
register.filter("update_rate",update_query("update_rate"))
register.filter("encode_query",encode_query)
register.filter("query_equals",query_equals)
