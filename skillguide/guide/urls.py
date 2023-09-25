from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('vacancies/', views.vacancies),
    path('vacancies/<int:vacancy_id>', views.vacancy),
    path('skills/', views.skills),
    path('skills/<int:skill_id>', views.skill),
    path('querys/', views.querys),
    path('query/<int:query_id>', views.query),
    path('analysis/', views.analysis),
    path('about/', views.about),
]