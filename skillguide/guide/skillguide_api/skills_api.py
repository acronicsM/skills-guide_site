import requests

from ..common import SERVER_ARD
from ..models import SkillColor

api_address = 'tags'
SKILLS_RESPONSE = {'pages': [], 'skills': []}


def skills(**kwargs):

    response = requests.get(f'{SERVER_ARD}/{api_address}', params=kwargs).json()

    max_page = response['found'] // kwargs['per_page'] + ((response['found'] % kwargs['per_page']) > 0)
    SKILLS_RESPONSE['pages'] = [{'page': i + 1, 'active': i == kwargs['page']} for i in range(max_page)]

    skill_response = []
    for j in response['result']:
        skill_name = j['name'].lower().strip()
        skill_obj = SkillColor.objects.filter(skill=skill_name).first()
        if not skill_obj:
            skill_obj = SkillColor.objects.create(skill=skill_name)
        skill_response.append({
            'name': f'{skill_obj.skill.capitalize()} | {j["vacancies"]}',
            'back': skill_obj.background,
            'color': skill_obj.color,
            'id': j['id']
        })

    SKILLS_RESPONSE['skills'] = skill_response

    return SKILLS_RESPONSE
