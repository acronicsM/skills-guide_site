from django import template


register = template.Library()


@register.inclusion_tag('guide/includes/admin/start_parser.html')
def start_parser():
    return None
