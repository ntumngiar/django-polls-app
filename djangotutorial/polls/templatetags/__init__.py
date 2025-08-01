from django import template

register = template.Library()


@register.filter
def is_recent(value):
    """
    Returns a colored span based on whether the question was published recently.
    """
    if value:
        return '<span style="color: green;">✓</span>'
    else:
        return '<span style="color: red;">✗</span>'
