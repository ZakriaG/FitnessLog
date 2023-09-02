from django import template

register = template.Library()

@register.filter
def addstr(arg1, arg2):
    """concatenate arg1 & arg2"""
    return str(arg1) + str(arg2)

@register.simple_tag(takes_context=True)
def get_by_name(context, name):
    if name not in context:
        return None
    return context[name]