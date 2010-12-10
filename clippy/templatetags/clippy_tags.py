"""
clippy.py - clippy template tag
"""

from django import template
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def clippy(text):
    """
    Generates a clippy html code

    param:
        text => text to generate the html code from

    """
    return mark_safe(render_to_string('clippy.html', {'text': text, 'MEDIA_URL': settings.MEDIA_URL}).rstrip())
