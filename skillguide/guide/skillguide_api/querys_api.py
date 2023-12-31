import requests

from ..common import SERVER_ARD, formatted_salary

api_address = 'job_search_queries'
QUERYS_RESPONSE = dict()


def querys(**kwargs):
    return {
        i['id']:
            {
                'count': i['count'],
                'name': i['name'],
                'salary': f'{formatted_salary(i["min"], "от")} {formatted_salary(i["max"], "до")}',
            }
        for i in requests.get(f'{SERVER_ARD}/{api_address}', params=kwargs).json()['queries']
    }
