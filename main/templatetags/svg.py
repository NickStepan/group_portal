import os
from django import template
from django.conf import settings
from django.utils.safestring import mark_safe
import re

register = template.Library()


@register.simple_tag
def loadsvg(path):
    full_path = os.path.join(settings.STATICFILES_DIRS[0], path)

    try:
        with open(full_path, 'r', encoding='utf-8') as file:
            svg_content = file.read()

        svg_content = re.sub(r"<\s*\?xml\s*.*\?\s*>", "", svg_content)

        return mark_safe(svg_content)
    except FileNotFoundError:
        return ''
