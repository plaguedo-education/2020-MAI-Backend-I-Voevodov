from django.urls import path
from . import views

urlpatterns = [
    path('', views.CompaniesView.as_view(), name='companies_list'),
    path('<uuid:pk>', views.CompanyDetailView.as_view(), name='companie_detail'),
    path('all/', views.CompaniesAllHtmlView.as_view(), name='companie_all_html'),
    path('new/', views.CompanyNewView.as_view(), name='companie_new'),
    path('vacancies/all/', views.VacancyAllHtmlView.as_view(), name='vacancies_all_html'),
    path('vacancies/<uuid:pk>', views.VacancyDetailView.as_view(), name='vacancy_detail'),
    #path('vacancies/response', views.VacancyResponseView.as_view(), name='vacancy_response'),
]