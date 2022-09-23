"""vacancies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import VacanciesView
from companies.views import CompaniesView
from custom_auth.views import RegisterView, LoginView
from employee.views import EmployeeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('companies/', CompaniesView.as_view({'get': 'list', 'post': 'create'})),
    path('companies/<int:pk>/', CompaniesView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('', VacanciesView.as_view({'get': 'list', 'post': 'create'})),
    path('vacancy/<int:pk>/', VacanciesView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('employee/', EmployeeView.as_view({'get': 'list', 'post': 'create'})),
    path('employee/<int:pk>/', EmployeeView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
]
