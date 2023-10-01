import requests
from django.shortcuts import render
from django.http import HttpResponseNotFound
from guide.common import index_dict, SERVER_ARD, formatted_salary, string_hh_to_datetime, BACK, COLOR


def index(request):
    data = index_dict()

    response = requests.get(f'{SERVER_ARD}').json()

    for i in response['top_vacancies']:
        salary_from = formatted_salary(i["salary_from"], "от")
        salary_to = formatted_salary(i["salary_to"], "до")

        i['salary'] = f'{salary_from} {salary_to}'

    for i in response['top_skills']:
        i['min'] = formatted_salary(i["min"], "от")
        i['max']= formatted_salary(i["max"], "до")

    data['response'] = response

    return render(request, 'guide/index.html', context=data)


def vacancies(request):
    data = index_dict()

    params = {
        'page': request.GET.get('page') if request.GET.get('page') else 0,
        'per_page': request.GET.get('per_page') if request.GET.get('per_page') else 10,
        'tag_id': request.GET.get('tag_id') if request.GET.get('tag_id') else None,
        'query': request.GET.get('query') if request.GET.get('query') else None,
    }

    response = requests.get(f'{SERVER_ARD}/vacancies', params=params).json()

    max_page = response['found'] // params['per_page'] + ((response['found'] % params['per_page']) > 0)

    data['pages'] = [{'page': i + 1, 'active': i == params['page']} for i in range(max_page)]
    data['url_name'] = 'vacancies'
    data['vacancies'] = []

    for i in response['result']:
        response = requests.get(f'{SERVER_ARD}/get_vacancy_tags/{i["id"]}').json()

        salary_from = formatted_salary(i["salary_from"], "от")
        salary_to = formatted_salary(i["salary_to"], "до")

        _skills = [{'name': j['name'], 'back': BACK, 'color': COLOR, 'id': j['id']} for j in response]

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
    data['skills'] = []
    data['pages'] = []
    data['url_name'] = 'skills'

    per_page = 100
    page = 0
    if request.GET:
        page = int(request.GET.get('page')) - 1

    url = f'{SERVER_ARD}/tags?page={page}&per_page={per_page}'
    response = requests.get(url).json()

    found, result = response['found'], response['result']

    max_page = found // per_page + ((found % per_page) > 0)

    _skills = [{'name': f'{j["name"]} | {j["vacancies"]}', 'back': BACK, 'color': COLOR, 'id': j['id']} for j in result]

    data['pages'] = [{'page': i + 1, 'active': i == page} for i in range(max_page)]
    data['skills'] = _skills

    return render(request, 'guide/skills.html', context=data)


def querys(request):
    data = index_dict()
    data['querys'] = requests.get(f'{SERVER_ARD}/query',).json()

    for k, v in data['querys'].items():
        v['salary'] = f'{formatted_salary(v["min"], "от")} {formatted_salary(v["max"], "до")}'

    return render(request, 'guide/querys.html', context=data)


def analysis(request):
    data = index_dict()

    return render(request, 'guide/analysis.html', context=data)


def about(request):
    data = index_dict()

    return render(request, 'guide/about.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound(f'Страница не найдена')
