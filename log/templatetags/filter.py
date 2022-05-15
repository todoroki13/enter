from django import template

register = template.Library()

@register.filter(name='split')
def split(value, key):
    return value.split(key)

@register.filter(name='embed')
def embed(value):
    x = value.find('/view?')
    value = value[0:x]
    return value