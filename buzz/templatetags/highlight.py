from django import template
from django.utils.safestring import mark_safe
from django.utils.html import escape

import re

register = template.Library()

def highlight(text,words):
    regexp = "(%s)" % "|".join(map(re.escape,words.split()))
    text = re.sub(regexp,r"<strong>\1</strong>",escape(text),flags=re.IGNORECASE)
    return mark_safe(text)

register.filter("highlight",highlight)
