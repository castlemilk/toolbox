from django import template

register  = template.Library()

register.filter('next')

def next(value, arg):
    try:
        return value[int(arg)+1]
    except:
        return None
