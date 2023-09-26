import requests
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from guide.common import index_dict, SERVER_ARD


def index(request):
    return render(request, 'guide/index.html', context=index_dict())


def vacancies(request):
    return HttpResponse('Вакансии')


def vacancy(request, vacancy_id):
    return HttpResponse(f'Вакансия №{vacancy_id}')


def skills(request):
    data = index_dict()

    page = 0
    if request.GET:
        page = 1

    url = f'{SERVER_ARD}/vacancies?page={page}'

    response = requests.get(url).json()
    data['vacancies'] = response['result']

    return render(request, 'guide/boot.html', context=data)


def skill(request, skill_id):
    return HttpResponse(f'Навык №{skill_id}')


def querys(request):
    return HttpResponse('Запросы')


def query(request, query_id):
    return HttpResponse(f'Запрос №{query_id}')


def analysis(request):
    return HttpResponse(f'Анализ навыков')


def about(request):
    return HttpResponse(f'О проекте')


def page_not_found(request, exception):
    return HttpResponseNotFound(f'Страница не найдена')
