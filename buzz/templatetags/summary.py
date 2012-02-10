# -*- coding: utf-8 -*-

import markdown
import re
import xml.etree.cElementTree as etree
from django.utils.safestring import mark_safe
from django import template
register = template.Library()

def treeToText(tree):
    text = tree.text or ""

    for child in tree:
        text += treeToText(child)

    text += tree.tail or ""
    return text

def getParagraphs(tree):
    if tree.tag in ("p","li","h1","h2","h3","h4","h5","h6","h7"):
        text = treeToText(tree)
        if len(text.split()) > 40:
            paragraphs = text.split(". ")
            for i in range(len(paragraphs)-1):
                paragraphs[i] += "."
            return paragraphs
        else:
            return [text]
    else:
        paragraphs = []
        for child in tree:
            paragraphs.extend(getParagraphs(child))

        return paragraphs



def match_score(m):
    if m is None: # No match at all
        return 0
    elif m.start(0) == 0 and m.end(0) == 0: # Exact word
        return 60
    elif m.start(0) == 0 or m.end(0) == 0: # Prefix/Sufix
        return 30
    else: # Substring
        return 10

def text_score(text,regexp):
    score = 0
    words = text.split()
    for word in words:
        score += match_score(regexp.search(text))

    score -= abs(len(words)-40) # We preffer medium-sized texts
    return score

def append_text(elm,text):
    if len(elm) == 0:
        if elm.text is None:
            elm.text = text
        else:
            elm.text += text
    else:
        if elm[-1].tail is None:
            elm[-1].tail = text
        else:
            elm[-1].tail += text

def append_marked_text(elm,klass,text):
    mark = etree.Element("span")
    mark.set("class", klass)
    mark.text = text
    elm.append(mark)

class MarkdownSummarize(markdown.treeprocessors.Treeprocessor):
    def run(self, root):
        regexp = re.compile("(%s)" % "|".join(map(re.escape, self.words)),re.IGNORECASE)
        allp = getParagraphs(root)
        scores = [(i,allp[i],text_score(allp[i],regexp)) for i in range(len(allp))]
        scores.sort(key=lambda x: x[2])
        paragraphs = scores[-3:] # Get the 3 with more score
        paragraphs.sort(key=lambda x: x[0]) # Order them in the document's order

        newroot = etree.Element("div")

        last_index = -1
        for index,text,score in paragraphs:
            if index > last_index+1:
                append_marked_text(newroot, "elipsis", u" […] ")

            parsed = 0
            for match in regexp.finditer(text):
                append_text(newroot,text[parsed:match.start()])
                append_marked_text(newroot, self.klass, match.group(1))
                parsed = match.end()

            append_text(newroot,text[parsed:])
            last_index = index

        if last_index < len(allp)-1:
            append_marked_text(newroot, "elipsis", u" […] ")

        return newroot

class SummarizeExtension(markdown.Extension):
    def __init__(self,words,klass):
        self.words = words
        self.klass = klass
    def extendMarkdown(self, md, md_globals):
        sm = MarkdownSummarize(md)
        sm.words = self.words
        sm.klass = self.klass
        md.treeprocessors.add("summarize", sm, "_end")

def summary_hightlight(value,query,klass="search_result"):
    words = query.split()
    extension = SummarizeExtension(words,klass)

    md = markdown.Markdown(extensions=[extension],safe_mode="escape")
    return mark_safe(md.convert(value))

def summary(value,mention):
    words = "mozilla"  # TODO: Move to settings
    if mention.product is not None:
        words += " " + mention.product.name

    return summary_hightlight(value,words,klass="")

register.filter("summary_hightlight",summary_hightlight)
register.filter("summary",summary)
