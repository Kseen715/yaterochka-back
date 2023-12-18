from .serializers import *
from .permission import IsAdminOrReadOnly, IsOwnerOrReadOnly
from io import BytesIO
import pandas as pd
from django.http import JsonResponse, HttpResponse
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import AllowAny


class ProductAPIList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)


class ProductAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)


class ProductAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly,)


class StoreAPIList(generics.ListCreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class StoreAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class StoreAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = (IsAdminOrReadOnly,)


class EmployeeAPIList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class EmployeeAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class EmployeeAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (IsAdminOrReadOnly,)


class GroupAPIList(generics.ListCreateAPIView):
    queryset = Groupp.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class GroupAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Groupp.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class GroupAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Groupp.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAdminOrReadOnly,)


class CheckAPIList(generics.ListCreateAPIView):
    queryset = Chek.objects.all()
    serializer_class = CheckSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CheckAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Chek.objects.all()
    serializer_class = CheckSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class CheckAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Chek.objects.all()
    serializer_class = CheckSerializer
    permission_classes = (IsAdminOrReadOnly,)


# Функция для получения данных в формате JSON
def get_data_as_json(request):
    data = Product.objects.all().values()
    return JsonResponse(list(data), safe=False)

# Функция для получения данных в формате CSV


def get_data_as_csv_product(request):
    data = Product.objects.all().values()  # Замените YourModel на вашу модель
    df = pd.DataFrame(list(data))
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="product.csv"'
    df.to_csv(path_or_buf=response, index=False)
    return response


def get_data_as_csv_store(request):
    data = Store.objects.all().values()  # Замените YourModel на вашу модель
    df = pd.DataFrame(list(data))
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="store.csv"'
    df.to_csv(path_or_buf=response, index=False)
    return response


def get_data_as_csv_employee(request):
    data = Employee.objects.all().values()  # Замените YourModel на вашу модель
    df = pd.DataFrame(list(data))
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="employee.csv"'
    df.to_csv(path_or_buf=response, index=False)
    return response


def get_data_as_csv_group(request):
    data = Groupp.objects.all().values()  # Замените YourModel на вашу модель
    df = pd.DataFrame(list(data))
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="group.csv"'
    df.to_csv(path_or_buf=response, index=False)
    return response


def get_data_as_csv_check(request):
    data = Chek.objects.all().values()  # Замените YourModel на вашу модель
    df = pd.DataFrame(list(data))
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="check.csv"'
    df.to_csv(path_or_buf=response, index=False)
    return response
