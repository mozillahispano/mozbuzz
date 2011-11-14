from django import template
import urllib
register = template.Library()

class DictPointer:
    def __init__(self,dict,key):
        self.dict = dict
        self.key = key
    def get(self):
        return self.dict[self.key]
    def set(self,val):
        self.dict[self.key] = val

def query_get(obj,key):
    return DictPointer(obj,key)

def query_toggle(obj,val):
    obj.dict = obj.dict.copy()
    elms = obj.get().copy()

    if val in elms:
        elms.remove(val)
    else:
        elms.add(val)

    obj.set(elms)
    return obj

def query_set(obj,val):
    new = obj.dict.copy()
    new[obj.key] = set([val])
    return new

def encode_query(obj):
    if isinstance(obj,DictPointer):
        obj = obj.dict

    tmp = {}
    for key,val in obj.iteritems():
        tmp[key] = query_encode_val(val)

    return urllib.urlencode(tmp)

def query_encode_val(val):
    if type(val) == set:
        return ",".join(map(str,val))
    else:
        return val

def query_contains(obj,val):
    return val in obj.get()



register.filter("query_get",query_get)
register.filter("query_set",query_set)
register.filter("query_encode",encode_query)
register.filter("query_encode_val",query_encode_val)
register.filter("query_toggle",query_toggle)
