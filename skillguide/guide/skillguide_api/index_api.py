import requests

from ..common import SERVER_ARD, formatted_salary

api_address = 'index'
EXCEPT_RESPONSE = {'count_vacancies': 0, 'count_skills': 0, 'top_vacancies': [], 'top_skills': []}


def index(**kwargs):
    adr = f'{SERVER_ARD}/{api_address}'

    response = requests.get(adr).json()

    for i in response['top_vacancies']:
        salary_from = formatted_salary(i["salary_from"], "от")
        salary_to = formatted_salary(i["salary_to"], "до")

        i['salary'] = f'{salary_from} {salary_to}'

    for i in response['top_skills']:
        i['min'] = formatted_salary(i["min"], "от")
        i['max'] = formatted_salary(i["max"], "до")

    return response
