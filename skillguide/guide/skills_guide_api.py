import requests

from .skillguide_api import INDEX_MODEL, VACANCIES_MODEL, VACANCY_MODEL, SKILLS_MODEL, QUERYS_MODEL, AGGREGATORS_MODEL

MODELS = {
    'index': INDEX_MODEL,
    'vacancies': VACANCIES_MODEL,
    'vacancy': VACANCY_MODEL,
    'tags': SKILLS_MODEL,
    'querys': QUERYS_MODEL,
    'aggregators': AGGREGATORS_MODEL,
}


def get_api_response(model_name: str, **kwargs):
    model = MODELS[model_name]
    response, func = model['response'], model['func']

    try:
        return func(**kwargs)
    except requests.ConnectionError:
        return response
