from django import template

register = template.Library()

@register.filter(is_safe=True)
def phone(value):
    return f"{value[:2]}+ {value[2:9]}-{value[9:]}"