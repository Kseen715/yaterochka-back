from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    expiration_date = models.DateField()
    price = models.IntegerField()
    user = models.ForeignKey(User, verbose_name='User',
                             on_delete=models.CASCADE)


class Store(models.Model):
    id = models.IntegerField(primary_key=True)
    store_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    user = models.ForeignKey(User, verbose_name='User',
                             on_delete=models.CASCADE)


class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    # store_id = models.ForeignKey(Store, verbose_name='store_id',on_delete=models.CASCADE)
    store_id = models.IntegerField()
    user = models.ForeignKey(User, verbose_name='User',
                             on_delete=models.CASCADE)


class Groupp(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=255)
    number = models.IntegerField()
    # product_id = models.ForeignKey(
    #     Product, verbose_name='product_id', on_delete=models.CASCADE)
    # store_id = models.ForeignKey(
    #     Store, verbose_name='store_id', on_delete=models.CASCADE)
    product_id = models.IntegerField()
    store_id = models.IntegerField()
    user = models.ForeignKey(User, verbose_name='User',
                             on_delete=models.CASCADE)


class Chek(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateField()
    time = models.TimeField()
    total = models.IntegerField()
    product_group_id = models.IntegerField()
    store_id = models.IntegerField()
    # store_id = models.ForeignKey(
    #     Store, verbose_name='store_id', on_delete=models.CASCADE)
    # product_group_id = models.ForeignKey(
    #     Groupp, verbose_name='product_group_id', on_delete=models.CASCADE)
    number_sold_group = models.IntegerField()
    user = models.ForeignKey(User, verbose_name='User',
                             on_delete=models.CASCADE)
