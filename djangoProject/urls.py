"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers

from meow.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('log/', include('rest_framework.urls')),
    path('product/', ProductAPIList.as_view()),
    path('product/<int:pk>/', ProductAPIUpdate.as_view()),
    path('product_del/<int:pk>/', ProductAPIDestroy.as_view()),
    path('product/get-csv-data/', get_data_as_csv_product),
    path('store/', StoreAPIList.as_view()),
    path('store/<int:pk>/', StoreAPIUpdate.as_view()),
    path('store_del/<int:pk>/', StoreAPIDestroy.as_view()),
    path('store/get-csv-data/', get_data_as_csv_store),
    path('employee/', EmployeeAPIList.as_view()),
    path('employee/<int:pk>/', EmployeeAPIUpdate.as_view()),
    path('employee_del/<int:pk>/', EmployeeAPIDestroy.as_view()),
    path('employee/get-csv-data/', get_data_as_csv_employee),
    path('group/', GroupAPIList.as_view()),
    path('group/<int:pk>/', GroupAPIUpdate.as_view()),
    path('group_del/<int:pk>/', GroupAPIDestroy.as_view()),
    path('group/get-csv-data/', get_data_as_csv_group),
    path('check/', CheckAPIList.as_view()),
    path('check/<int:pk>/', CheckAPIUpdate.as_view()),
    path('check_del/<int:pk>/', CheckAPIDestroy.as_view()),
    path('check/get-csv-data/', get_data_as_csv_check),
    path('get-json-data/', get_data_as_json),
]
