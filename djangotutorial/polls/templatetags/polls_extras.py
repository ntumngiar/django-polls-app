from django import template

register = template.Library()


@register.filter(name='is_recent')
def is_recent(value):
    """
    Returns a colored span based on whether the question was published recently.
    """
    if value:
        return 'Yes - Recent'
    else:
        return 'No - Older'
