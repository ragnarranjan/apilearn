#from django.db import models
#from rest_framework import fields
#from rest_framework.fields import Field
from .models import Employee
from rest_framework import serializers
from django.contrib.auth.models import User


#class EmployeeSerializer(serializers.Serializer):
    # name = serializers.CharField(max_length=30)
    # email = serializers.EmailField()
    # password = serializers.CharField(max_length=20)
    # phone = serializers.IntegerField()


    # def create(self, validated_data):
    #     print("validated data----------", validated_data)
    #     return Employee.objects.create(**validated_data)

    # # def update(self, employee, validated_data):
    # #     newEmployee = Employee(**validated_data)
    # #     newEmployee.save()
    # #     return newEmployee
    # def update(self, employee, validated_data):
    #     employee.name = validated_data.get('name', employee.name)
    #     employee.email = validated_data.get('email',employee.email)
    #     employee.password = validated_data.get('password', employee.password)
    #     employee.phone = validated_data.get('phone', employee.phone)
    #     employee.save()
    #     return employee
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

# class UserSerializer(serializers.Serializer):
    # username = serializers.CharField(max_length=100)
    # email = serializers.EmailField()
    # password = serializers.CharField(max_length =20)
    # first_name = serializers.CharField(max_length = 30)
    # last_name = serializers.CharField(max_length=20)
class UserSerializer(serializers.ModelSerializer):
    class  Meta:
        model = User
        fields = '__all__'





