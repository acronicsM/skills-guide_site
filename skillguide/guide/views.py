from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.views import View
from django.views.generic import ListView, TemplateView

from .gpt_api.latter import get_letter
from .skills_guide_api import get_api_response
from .skillguide_api import admin_api
from .models import UploadAPIImages


class GuideHome(ListView):
    template_name = 'guide/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Python Skills Tracker'
        context['images'] = {f.type_image: f.image.url
                             for f in UploadAPIImages.objects.filter(type_image__in=['salary', 'vacancies']).all()
                             }
        return context

    def get_queryset(self):
        return get_api_response('index')


class GuideVacancies(ListView):
    template_name = 'guide/vacancies.html'
    url_name = 'vacancies'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вакансии'
        context['url_name'] = self.url_name

        return context

    def get_queryset(self):
        params = {
            'page': (int(self.request.GET.get('page')) - 1) if self.request.GET.get('page') else 0,
            'per_page': self.request.GET.get('per_page') if self.request.GET.get('per_page') else 10,
            'tag_id': self.request.GET.get('tag_id') if self.request.GET.get('tag_id') else None,
            'query': self.request.GET.get('query') if self.request.GET.get('query') else None,
        }
        return get_api_response(self.url_name, **params)


class GuideVacancy(ListView):
    template_name = 'guide/vacancy.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vacancy_id'] = self.kwargs['vacancy_id']

        return context

    def get_queryset(self):
        return get_api_response('vacancy', vacancy_id=self.kwargs['vacancy_id'])


class CoverLetter(View):
    template_name = 'guide/vacancy_response.html'

    async def get(self, request, *args, **kwargs):
        context = await self.get_context_data(kwargs['vacancy_id'], kwargs['type_gpt'])
        return render(request, template_name=self.template_name, context=context)

    @staticmethod
    async def get_context_data(vacancy_id, type_gpt):
        context = dict()
        context['title'] = 'Сопроводительное письмо'
        context['vacancy_data'] = get_api_response('vacancy', vacancy_id=vacancy_id)
        context['vacancy_id'] = vacancy_id

        latter = await get_letter(context['vacancy_data'], type_gpt)

        context['latter'] = latter

        return context


class Interview(TemplateView):
    template_name = 'guide/vacancy_interview.html'
    extra_context = {
        'title': 'Тестовое собеседование',
    }


class GuideSkills(ListView):
    template_name = 'guide/skills.html'
    url_name = 'skills'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Навыки'
        context['url_name'] = self.url_name

        return context

    def get_queryset(self):
        params = {
            'page': self.request.GET.get('page') if self.request.GET.get('page') else 0,
            'per_page': self.request.GET.get('per_page') if self.request.GET.get('per_page') else 100,
        }
        return get_api_response('tags', **params)


class Queries(View):
    template_name = 'guide/querys.html'

    def get(self, request):
        if request.GET.get('start_parser') == 'True':
            admin_api.start_parser(request)
        elif query := request.GET.get('delete_queries'):
            admin_api.delete_queries(request, int(query))

        return render(request, template_name=self.template_name, context=self.get_context_data())

    def post(self, request):
        admin_api.add_queries(request)
        return render(request, template_name=self.template_name, context=self.get_context_data())

    @staticmethod
    def get_context_data():
        context = dict()
        context['title'] = 'Поисковые запросы'
        context['querys'] = get_api_response('querys')

        return context


class Aggregators(View):
    template_name = 'guide/aggregators.html'

    def get(self, request):
        if request.GET.get('start_parser') == 'True':
            admin_api.start_parser(request)
        elif aggregator := request.GET.get('delete_aggregators'):
            admin_api.delete_aggregators(request, aggregator)

        return render(request, template_name=self.template_name, context=self.get_context_data())

    def post(self, request):
        admin_api.add_aggregators(request)
        return render(request, template_name=self.template_name, context=self.get_context_data())

    @staticmethod
    def get_context_data():
        context = dict()
        context['title'] = 'Агрегаторы вакансий'
        context['aggregators'] = get_api_response('aggregators')

        return context


class Analysis(View):
    f_type = ['salary', 'vacancies']
    template_name = 'guide/analysis.html'

    def get(self, request):
        if request.GET.get('upload_images') == 'True':
            admin_api.upload_images(request)

        return render(request, template_name=self.template_name, context=self.get_context_data())

    def get_context_data(self):
        context = dict()
        context['title'] = 'Визуальный анализ навыков'
        context['images'] = {f.type_image: f.image.url for f in
                             UploadAPIImages.objects.filter(type_image__in=self.f_type).all()}

        return context


class About(TemplateView):
    template_name = 'guide/about.html'
    extra_context = {
        'title': 'О проекте',
    }


def page_not_found(request, exception):
    return HttpResponseNotFound(f'Страница не найдена')
