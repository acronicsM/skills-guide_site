import requests

from ..common import SERVER_ARD, formatted_salary, BACK, COLOR, string_hh_to_datetime

coming_soon = 'coming soon'
api_address = 'vacancies'
api_vacancy_tags = 'tags'

VACANCIES_RESPONSE = {'pages': [], 'vacancies': []}
VACANCY_RESPONSE = {
    'description': coming_soon,
    'employment': coming_soon,
    'experience': coming_soon,
    'name': coming_soon,
    'date': coming_soon,
    'schedule': coming_soon,
    'salary': coming_soon,
    'skills': coming_soon,
}


def vacancies(**kwargs):
    response = requests.get(f'{SERVER_ARD}/{api_address}', params=kwargs).json()

    max_page = response['found'] // kwargs['per_page'] + ((response['found'] % kwargs['per_page']) > 0)

    VACANCIES_RESPONSE['pages'] = [{'page': i + 1, 'active': i == kwargs['page']} for i in range(max_page)]

    for i in response['result']:
        salary_from = formatted_salary(i["salary_from"], "от")
        salary_to = formatted_salary(i["salary_to"], "до")

        VACANCIES_RESPONSE['vacancies'].append({
            'id': i['id'],
            'name': i['name'],
            'salary': f'{salary_from} {salary_to}',
            'date': string_hh_to_datetime(i['published_at']),
            'requirement': i['requirement'],
            'skills': vacancy_skills(i["id"]),
        })

    return VACANCIES_RESPONSE


def vacancy_skills(vacancy_id: int):
    response = requests.get(f'{SERVER_ARD}/{api_address}/{vacancy_id}/{api_vacancy_tags}').json()

    return [{'name': j['name'], 'back': BACK, 'color': COLOR, 'id': j['id']} for j in response['skills']]


def vacancy(vacancy_id: int):
    response = requests.get(f'{SERVER_ARD}/{api_address}/{vacancy_id}').json()

    salary_from = formatted_salary(response["salary_from"], "от")
    salary_to = formatted_salary(response["salary_to"], "до")

    VACANCY_RESPONSE['description'] = response['description']
    VACANCY_RESPONSE['employment'] = response['employment']
    VACANCY_RESPONSE['experience'] = response['experience']
    VACANCY_RESPONSE['name'] = response['name']
    VACANCY_RESPONSE['date'] = string_hh_to_datetime(response['published_at'])
    VACANCY_RESPONSE['schedule'] = response['schedule']
    VACANCY_RESPONSE['salary'] = f'{salary_from} {salary_to}'
    VACANCY_RESPONSE['skills'] = vacancy_skills(vacancy_id)

    return VACANCY_RESPONSE
