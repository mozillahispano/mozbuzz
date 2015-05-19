import os

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name='basename')
@stringfilter
def basename(value):
    return os.path.basename(value)


@register.filter(name='get_extension')
@stringfilter
def get_extension(value):
    return os.path.splitext(value)[1]


@register.filter(name='is_image')
@stringfilter
def is_image(value):
    
    types = [
    	'.jpg','.jpeg', '.png',
    	'.gif', '.ico','.bmp'
    ]	

    if value in types:
    	return True
    else:
    	return False
