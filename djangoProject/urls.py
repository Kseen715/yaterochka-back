from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.views.generic import RedirectView

from meow.views import *

router_store = routers.SimpleRouter()
router_store.register(r'store', StoreAPIList)

router_product = routers.SimpleRouter()
router_product.register(r'product', ProductAPIList)

router_employee = routers.SimpleRouter()
router_employee.register(r'employee', EmployeeAPIList)

router_group = routers.SimpleRouter()
router_group.register(r'group', GroupAPIList)

router_check = routers.SimpleRouter()
router_check.register(r'check', CheckAPIList)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('log/', include('rest_framework.urls')),
    path('sel/', include(router_store.urls)),
    path('sel/', include(router_product.urls)),
    path('sel/', include(router_employee.urls)),
    path('sel/', include(router_group.urls)),
    path('sel/', include(router_check.urls)),
    path('get-json-data/sel/product/', get_data_as_json_product),
    path('get-json-data/sel/group/', get_data_as_json_group),
    path('get-json-data/sel/check/', get_data_as_json_check),
    path('get-json-data/sel/employee/', get_data_as_json_employee),
    path('get-json-data/sel/store/', get_data_as_json_store),
    path('get-csv-data/sel/product/', get_data_as_csv_product),
    path('get-csv-data/sel/group/', get_data_as_csv_group),
    path('get-csv-data/sel/check/', get_data_as_csv_check),
    path('get-csv-data/sel/employee/', get_data_as_csv_employee),
    path('get-csv-data/sel/store/', get_data_as_csv_store),
    path('user-status/', UserStatusView.as_view(), name='user-status'),
    path('accounts/profile/', RedirectView.as_view(url='http://localhost')),
    path('admin/', RedirectView.as_view(url='http://localhost')),
]
