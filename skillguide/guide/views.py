from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def index(request):
    return HttpResponse('Главная')


def vacancies(request):
    return HttpResponse('Вакансии')


def vacancy(request, vacancy_id):
    return HttpResponse(f'Вакансия №{vacancy_id}')


def skills(request):
    return HttpResponse('Навыки')


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


def page_not_found(request):
    return HttpResponseNotFound(f'Страница не найдена')
