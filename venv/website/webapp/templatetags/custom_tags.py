from django.template.defaulttags import register


@register.filter
def get_value(dictionary, key):
    return (dictionary[key])


@register.filter
def capitalize(value):
    return value.capitalize()
