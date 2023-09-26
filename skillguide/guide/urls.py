from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('vacancies/', views.vacancies, name='vacancies'),
    path('vacancies/<int:vacancy_id>', views.vacancy, name='vacancy'),
    path('skills/', views.skills, name='skills'),
    path('skills/<int:skill_id>', views.skill, name='skill'),
    path('querys/', views.querys, name='querys'),
    path('query/<int:query_id>', views.query, name='query'),
    path('analysis/', views.analysis, name='analysis'),
    path('about/', views.about, name='about'),
]