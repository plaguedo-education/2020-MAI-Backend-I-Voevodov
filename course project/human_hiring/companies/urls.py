from django.urls import path
from . import views

urlpatterns = [
    path('', views.CompaniesView.as_view(), name='companies_list'),
    path('<uuid:pk>', views.CompanyDetailView.as_view(), name='companie_detail'),
    path('new/', views.CompanyNewView.as_view(), name='companie_new'),
]