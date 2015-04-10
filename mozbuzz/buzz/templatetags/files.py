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