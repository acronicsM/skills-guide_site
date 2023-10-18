import requests

from ..common import SERVER_ARD, BACK, COLOR

api_address = 'tags'
SKILLS_RESPONSE = {'pages': [], 'skills': []}


def skills(**kwargs):

    response = requests.get(f'{SERVER_ARD}/{api_address}', params=kwargs).json()

    max_page = response['found'] // kwargs['per_page'] + ((response['found'] % kwargs['per_page']) > 0)
    SKILLS_RESPONSE['pages'] = [{'page': i + 1, 'active': i == kwargs['page']} for i in range(max_page)]

    SKILLS_RESPONSE['skills'] = [
        {'name': f'{j["name"]} | {j["vacancies"]}', 'back': BACK, 'color': COLOR, 'id': j['id']}
        for j in response['result']
    ]

    return SKILLS_RESPONSE
