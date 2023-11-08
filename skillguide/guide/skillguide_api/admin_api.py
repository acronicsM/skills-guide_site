import requests

from django.contrib import messages

from ..common import SERVER_ARD
from ..forms import AddQueriesForm, AddAggregatorsForm


def start_parser(request):
    try:
        response = requests.get(f'{SERVER_ARD}/update_vacancies')
        response_data = response.json()
        data_text = f'Удалено: {response_data["delete_vacancies"]}\nНовых вакансий: {response_data["result"]["new_vacancies"]}\n'
        messages.info(request, f'{response.status_code}\n{data_text}')
    except ConnectionError:
        messages.error(request, 'Ошибка запуска парсера')


def add_queries(request):
    form = AddQueriesForm(request.POST)
    if form.is_valid():
        try:
            response = requests.post(f'{SERVER_ARD}/job_search_queries', json=form.cleaned_data)
            if response.status_code != requests.codes.created:
                messages.info(request, f'{response.status_code} Добавление запроса не было выполнено')
        except ConnectionError:
            messages.warning(request, 'Ошибка добавления поискового запроса')


def delete_queries(request, id: int):
    try:
        response = requests.delete(f'{SERVER_ARD}/job_search_queries', json={'id': id})
        if response.status_code != requests.codes.ok:
            messages.info(request, f'{response.status_code} Удаление запроса не было выполнено')
    except ConnectionError:
        messages.warning(request, 'Ошибка удаления поискового запроса')


def add_aggregators(request):
    form = AddAggregatorsForm(request.POST)
    if form.is_valid():
        try:
            response = requests.post(f'{SERVER_ARD}/aggregators', json=form.cleaned_data)
            if response.status_code != requests.codes.created:
                messages.info(request, f'{response.status_code} Добавление агрегатора не было выполнено')
        except ConnectionError:
            messages.warning(request, 'Ошибка добавления агрегатора')


def delete_aggregators(request, id: str):
    try:
        response = requests.delete(f'{SERVER_ARD}/aggregators', json={'id': id})
        if response.status_code != requests.codes.ok:
            messages.info(request, f'{response.status_code} Удаление агрегатора не было выполнено')
    except ConnectionError:
        messages.warning(request, 'Ошибка удаления агрегатора')
