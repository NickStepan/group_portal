from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def get_key(dictionary, key1_key2):
    try:
        return dictionary.get(key1_key2)
    except (ValueError, AttributeError):
        return ''