import requests

from django.shortcuts import render
from django.http import HttpResponseNotFound

from .common import index_dict, SERVER_ARD, formatted_salary, string_hh_to_datetime, BACK, COLOR
from .skills_guide_api import get_api_response


def index(request):
    data = index_dict()
    data['response'] = get_api_response('index')

    return render(request, 'guide/index.html', context=data)


def vacancies(request):
    data = index_dict()

    data['url_name'] = 'vacancies'

    params = {
        'page': request.GET.get('page') if request.GET.get('page') else 0,
        'per_page': request.GET.get('per_page') if request.GET.get('per_page') else 10,
        'tag_id': request.GET.get('tag_id') if request.GET.get('tag_id') else None,
        'query': request.GET.get('query') if request.GET.get('query') else None,
    }
    response = get_api_response('vacancies', **params)

    data['pages'] = response['pages']
    data['vacancies'] = response['vacancies']

    return render(request, 'guide/vacancies.html', context=data)


def vacancy(request, vacancy_id):
    data = index_dict()

    data['vacancy_data'] = get_api_response('vacancy', vacancy_id=vacancy_id)

    return render(request, 'guide/vacancy.html', context=data)


def skills(request):
    data = index_dict()
    data['url_name'] = 'skills'

    params = {
        'page': request.GET.get('page') if request.GET.get('page') else 0,
        'per_page': request.GET.get('per_page') if request.GET.get('per_page') else 100,
    }
    response = get_api_response('tags', **params)

    data['pages'] = response['pages']
    data['skills'] = response['skills']

    return render(request, 'guide/skills.html', context=data)


def querys(request):
    data = index_dict()
    data['querys'] = get_api_response('querys')

    return render(request, 'guide/querys.html', context=data)


def analysis(request):
    data = index_dict()

    return render(request, 'guide/analysis.html', context=data)


def about(request):
    data = index_dict()

    return render(request, 'guide/about.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound(f'Страница не найдена')
