import requests

from ..common import SERVER_ARD

api_address = 'aggregators'
AGGREGATORS_RESPONSE = dict()


def aggregators(**kwargs):
    return [i['id'] for i in requests.get(f'{SERVER_ARD}/{api_address}', params=kwargs).json()['aggregators']]
