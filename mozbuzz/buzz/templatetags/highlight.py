from django import template
from django.utils.safestring import mark_safe
from django.utils.html import escape

import re

register = template.Library()

def highlight(text,words):
    regexp = "(%s)" % "|".join(map(re.escape,words.split()))

    strings = []
    parsed = 0
    for match in re.finditer(regexp,text,flags=re.IGNORECASE):
        strings.append(escape(text[parsed:match.start()]))
        strings.append(r"<strong>%s</strong>" % escape(match.group(1)))
        parsed = match.end()
    strings.append(text[parsed:])

    return mark_safe("".join(strings))

register.filter("highlight",highlight)
