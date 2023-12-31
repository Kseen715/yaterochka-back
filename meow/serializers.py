from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Product
        fields = "__all__"


class StoreSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Store
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    phone = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = '__all__'

    def get_phone(self, obj):
        if self.context['request'].user.is_authenticated:
            return obj.phone
        else:
            return '***'


class GroupSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Groupp
        fields = "__all__"


class CheckSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Chek
        fields = "__all__"
