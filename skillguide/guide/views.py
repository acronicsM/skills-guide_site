import requests
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from guide.common import index_dict, SERVER_ARD, formatted_salary, string_hh_to_datetime


def index(request):
    return render(request, 'guide/index.html', context=index_dict())


def vacancies(request):
    data = index_dict()
    per_page = 10
    page = 0
    if request.GET:
        page = int(request.GET.get('page')) - 1

    url = f'{SERVER_ARD}/vacancies?page={page}&per_page={per_page}'

    response = requests.get(url).json()

    max_page = response['found'] // per_page + ((response['found'] % per_page) > 0)

    data['pages'] = [{'page': i + 1, 'active': i == page} for i in range(max_page)]
    data['vacancies'] = []

    for i in response['result']:
        response = requests.get(f'{SERVER_ARD}/get_vacancy_tags/{i["id"]}').json()

        salary_from = formatted_salary(i["salary_from"], "от")
        salary_to = formatted_salary(i["salary_to"], "до")

        _skills = [{'name': j['name'], 'back': '#ff6347', 'color': '#f5f5f5'} for j in response]

        data['vacancies'].append({
            'id': i['id'],
            'name': i['name'],
            'salary': f'{salary_from} {salary_to}',
            'date': string_hh_to_datetime(i['published_at']),
            'requirement': i['requirement'],
            'skills': _skills,
        })

    return render(request, 'guide/vacancies.html', context=data)


def vacancy(request, vacancy_id):
    data = index_dict()

    url = f'{SERVER_ARD}/get_vacancy/{vacancy_id}'
    response = requests.get(url).json()

    _skills = requests.get(f'{SERVER_ARD}/get_vacancy_tags/{vacancy_id}').json()
    _skills = [{'name': j['name'], 'back': '#ff6347', 'color': '#f5f5f5'} for j in _skills]

    salary_from = formatted_salary(response["salary_from"], "от")
    salary_to = formatted_salary(response["salary_to"], "до")

    data['vacancy_data'] = {
        'description': response['description'],
        'employment': response['employment'],
        'experience': response['experience'],
        'name': response['name'],
        'date': string_hh_to_datetime(response['published_at']),
        'schedule': response['schedule'],
        'salary': f'{salary_from} {salary_to}',
        'skills': _skills,
    }

    return render(request, 'guide/vacancy.html', context=data)


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
