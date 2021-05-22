from django.urls import path
from . import views

urlpatterns = [
    path('', views.CompaniesView.as_view(), name='companies_list'),
    path('<uuid:pk>', views.companie_detail, name='companie_detail'),
]