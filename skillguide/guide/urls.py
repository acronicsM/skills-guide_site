from django.urls import path
from . import views

urlpatterns = [
    path('', views.GuideHome.as_view(), name='home'),
    path('vacancies/', views.GuideVacancies.as_view(), name='vacancies'),
    path('vacancies/<int:vacancy_id>', views.GuideVacancy.as_view(), name='vacancy'),
    path('skills/', views.GuideSkills.as_view(), name='skills'),
    path('querys/', views.Queries.as_view(), name='querys'),
    path('aggregators/', views.Aggregators.as_view(), name='aggregators'),
    path('analysis/', views.Analysis.as_view(), name='analysis'),
    path('about/', views.About.as_view(), name='about'),
    path('vacancy_response/<int:vacancy_id>/<type_gpt>', views.CoverLetter.as_view(), name='response'),
    path('vacancy_interview', views.Interview.as_view(), name='interview'),
]
