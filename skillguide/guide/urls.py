from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('vacancies/', views.vacancies, name='vacancies'),
    path('vacancies/<int:vacancy_id>', views.vacancy, name='vacancy'),
    path('skills/', views.skills, name='skills'),
    path('querys/', views.querys, name='querys'),
    path('aggregators/', views.aggregators, name='aggregators'),
    path('analysis/', views.analysis, name='analysis'),
    path('about/', views.about, name='about'),
    path('vacancy_response/<int:vacancy_id>/<type_gpt>', views.vacancy_response, name='response'),
    path('vacancy_interview', views.interview, name='interview'),
]
