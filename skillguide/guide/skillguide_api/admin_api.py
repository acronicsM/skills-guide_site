import requests
from io import BytesIO
from zipfile import ZipFile
from datetime import date
from pathlib import Path

from django.contrib import messages
from django.contrib.staticfiles.storage import settings
from django.core.files.storage import default_storage

from ..common import SERVER_ARD
from ..forms import AddQueriesForm, AddAggregatorsForm
from ..models import UploadAPIImages


def start_parser(request):
    try:
        response = requests.get(f'{SERVER_ARD}/update_vacancies')
        response_data = response.json()
        data_text = f'Удалено: {response_data["delete_vacancies"]}\nНовых вакансий: {response_data["result"]["new_vacancies"]}\n'
        messages.info(request, f'{response.status_code}\n{data_text}')
    except ConnectionError:
        messages.error(request, 'Ошибка запуска парсера')


def upload_images(request):
    try:
        today = date.today()
        response = requests.get(f'{SERVER_ARD}/images')
        file_path = default_storage.path(f"{ settings.MEDIA_ROOT}/api/{today.year}/{today.month}/{today.day:02}/")

        if response.status_code == 200:
            with ZipFile(BytesIO(response.content)) as zip_file:
                zip_file.extractall(file_path)
                zip_file.close()

            del response

            for jpg_file in Path(file_path).glob('*.jpg'):
                f_type = jpg_file.name.split('.')[0]
                fp = UploadAPIImages.objects.filter(type_image=f_type).first()

                if not fp:
                    fp = UploadAPIImages(type_image=f_type)

                fp.image = str(jpg_file)
                fp.save()
        else:
            messages.warning(request, 'Ошибка загрузки изображений')

    except ConnectionError:
        messages.error(request, 'Ошибка загрузки изображений')


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
