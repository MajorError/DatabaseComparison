from django.conf import settings
import re
from django import template
from django.conf import settings

numeric_test = re.compile("^\d+$")
register = template.Library()

@register.filter
def get(value, key):
    if hasattr(value, str(key)):
        return getattr(value, key)
    elif hasattr(value, 'has_key') and value.has_key(key):
        return value[key]
    elif numeric_test.match(str(key)) and len(value) > int(key):
        return value[int(key)]
    else:
        return settings.TEMPLATE_STRING_IF_INVALID
