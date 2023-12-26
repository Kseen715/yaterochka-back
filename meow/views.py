from djangoProject.settings import ERR_LINK
from io import BytesIO
import pandas as pd
from django.http import JsonResponse, HttpResponse
from requests import Response
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from django.contrib.admin.views.decorators import staff_member_required
from .permission import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import *
from django.contrib.auth.decorators import permission_required
from rest_framework.views import APIView
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

methods = ['get', 'post', 'head',
           'put', 'patch', 'delete', 'update', 'destroy']


class UserStatusView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'is_authenticated': request.user.is_authenticated})

# def logout_view(request):
#     logout(request)
#     return HttpResponseRedirect("http://www.example.com")

class ProductAPIList(viewsets.ModelViewSet):
    http_method_names = methods
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class StoreAPIList(viewsets.ModelViewSet):
    http_method_names = methods
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class EmployeeAPIList(viewsets.ModelViewSet):
    http_method_names = methods
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class GroupAPIList(viewsets.ModelViewSet):
    http_method_names = methods
    queryset = Groupp.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class CheckAPIList(viewsets.ModelViewSet):
    http_method_names = methods
    queryset = Chek.objects.all()
    serializer_class = CheckSerializer
    permission_classes = (IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


# Функция для получения данных в формате JSON
def create_json(data, name):
    df = pd.DataFrame(list(data))
    response = HttpResponse(content_type='text/json')
    response['Content-Disposition'] = 'attachment; filename="' + name + '"'
    df.to_json(path_or_buf=response, orient='records')
    return response


@permission_required('app_name.change_product', login_url=ERR_LINK)
def get_data_as_json_product(request):
    data = Product.objects.all().values()
    return create_json(data, 'product.json')


@permission_required('app_name.change_product', login_url=ERR_LINK)
def get_data_as_json_store(request):
    data = Store.objects.all().values()
    return create_json(data, 'store.json')


@permission_required('app_name.change_product', login_url=ERR_LINK)
def get_data_as_json_group(request):
    data = Groupp.objects.all().values()
    return create_json(data, 'group.json')


@permission_required('app_name.change_product', login_url=ERR_LINK)
def get_data_as_json_employee(request):
    data = Employee.objects.all().values()
    return create_json(data, 'employee.json')


@permission_required('app_name.change_product', login_url=ERR_LINK)
def get_data_as_json_check(request):
    data = Chek.objects.all().values()
    return create_json(data, 'check.json')


# Функция для получения данных в формате CSV
def create_csv(data, name):
    df = pd.DataFrame(list(data))
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="' + name + '"'
    df.to_csv(path_or_buf=response, index=False)
    return response


@permission_required('app_name.change_product', login_url=ERR_LINK)
def get_data_as_csv_product(request):
    data = Product.objects.all().values()
    return create_csv(data, 'product.csv')


@permission_required('app_name.change_product', login_url=ERR_LINK)
def get_data_as_csv_check(request):
    data = Chek.objects.all().values()
    return create_csv(data, 'check.csv')


@permission_required('app_name.change_product', login_url=ERR_LINK)
def get_data_as_csv_group(request):
    data = Groupp.objects.all().values()
    return create_csv(data, 'group.csv')


@permission_required('app_name.change_product', login_url=ERR_LINK)
def get_data_as_csv_employee(request):
    data = Employee.objects.all().values()
    return create_csv(data, 'employee.csv')


@permission_required('app_name.change_product', login_url=ERR_LINK)
def get_data_as_csv_store(request):
    data = Store.objects.all().values()
    return create_csv(data, 'store.csv')
