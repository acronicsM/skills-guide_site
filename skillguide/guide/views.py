from django.shortcuts import render
from django.http import HttpResponseNotFound

from .gpt_api.latter import get_letter
from .common import index_dict
from .skills_guide_api import get_api_response
from .skillguide_api import admin_api
from .models import UploadAPIImages


def index(request):

    f_type = ['salary', 'vacancies']

    data_dict = index_dict()
    data_dict['response'] = get_api_response('index')
    data_dict['images'] = {f.type_image: f.image.url for f in UploadAPIImages.objects.filter(type_image__in=f_type).all()}

    return render(request, 'guide/index.html', context=data_dict)


def vacancies(request):
    data_dict = index_dict()

    data_dict['url_name'] = 'vacancies'

    params = {
        'page': (int(request.GET.get('page')) - 1) if request.GET.get('page') else 0,
        'per_page': request.GET.get('per_page') if request.GET.get('per_page') else 10,
        'tag_id': request.GET.get('tag_id') if request.GET.get('tag_id') else None,
        'query': request.GET.get('query') if request.GET.get('query') else None,
    }
    response = get_api_response('vacancies', **params)

    data_dict['pages'] = response['pages']
    data_dict['vacancies'] = response['vacancies']

    return render(request, 'guide/vacancies.html', context=data_dict)


def vacancy(request, vacancy_id):
    data_dict = index_dict()

    data_dict['vacancy_data'] = get_api_response('vacancy', vacancy_id=vacancy_id)
    data_dict['vacancy_id'] = vacancy_id

    return render(request, 'guide/vacancy.html', context=data_dict)


async def vacancy_response(request, vacancy_id, type_gpt):
    data_dict = index_dict()

    data_dict['vacancy_data'] = get_api_response('vacancy', vacancy_id=vacancy_id)
    data_dict['vacancy_id'] = vacancy_id

    latter = await get_letter(data_dict['vacancy_data'], type_gpt)

    data_dict['latter'] = latter

    return render(request, 'guide/vacancy_response.html', context=data_dict)


def interview(request):
    data_dict = index_dict()

    return render(request, 'guide/vacancy_interview.html', context=data_dict)


def skills(request):
    data_dict = index_dict()
    data_dict['url_name'] = 'skills'

    params = {
        'page': request.GET.get('page') if request.GET.get('page') else 0,
        'per_page': request.GET.get('per_page') if request.GET.get('per_page') else 100,
    }
    response = get_api_response('tags', **params)

    data_dict['pages'] = response['pages']
    data_dict['skills'] = response['skills']

    return render(request, 'guide/skills.html', context=data_dict)


def querys(request):
    if request.method == 'GET':
        if 'start_parser' in request.GET and request.GET['start_parser'] == 'True':
            admin_api.start_parser(request)
        elif 'delete_queries' in request.GET:
            admin_api.delete_queries(request, int(request.GET['delete_queries']))
    elif request.method == 'POST':
        admin_api.add_aggregators(request)

    data_dict = index_dict()
    data_dict['querys'] = get_api_response('querys')

    return render(request, 'guide/querys.html', context=data_dict)


def aggregators(request):
    if request.method == 'GET':
        if 'start_parser' in request.GET and request.GET['start_parser'] == 'True':
            admin_api.start_parser(request)
        elif 'delete_aggregators' in request.GET:
            admin_api.delete_aggregators(request, request.GET['delete_aggregators'])
    elif request.method == 'POST':
        admin_api.add_aggregators(request)

    data_dict = index_dict()
    data_dict['aggregators'] = get_api_response('aggregators')
    return render(request, 'guide/aggregators.html', context=data_dict)


def analysis(request):
    if request.method == 'GET' and 'upload_images' in request.GET and request.GET['upload_images'] == 'True':
        admin_api.upload_images(request)

    f_type = ['salary', 'vacancies']

    data_dict = index_dict()
    data_dict['response'] = get_api_response('index')
    data_dict['images'] = {f.type_image: f.image.url for f in
                           UploadAPIImages.objects.filter(type_image__in=f_type).all()}

    return render(request, 'guide/analysis.html', context=data_dict)


def about(request):
    data_dict = index_dict()

    return render(request, 'guide/about.html', context=data_dict)


def page_not_found(request, exception):
    return HttpResponseNotFound(f'Страница не найдена')
