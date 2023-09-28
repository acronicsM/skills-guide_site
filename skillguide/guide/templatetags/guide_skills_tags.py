from django import template


register = template.Library()


@register.inclusion_tag('guide/includes/skills_tags.html')
def skills_tags(skill_list: list):
    return {'skills': skill_list}
