from django import template
from django.utils.safestring import SafeUnicode
import re

register = template.Library()

@register.filter
def delineate_soup(list):
    str = "<br />&#9832;<br />".join(list)
    su = SafeUnicode(str)
    return su

@register.simple_tag
def active(request, pattern):

    path = request.path

    if path == '/':
        path = '/pret'

    if pattern == path:
        return ' class="current"'
    return ''
