from re import I
from django.contrib.auth.models import User
from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee
from .serializers import EmployeeSerializer , UserSerializer
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
@api_view(['GET','POST'])
#@csrf_exempt
def employeeListViews(request):
    if request.method =='GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees ,many = True )
        #return JsonResponse(serializer.data ,safe=False)
        return Response(serializer.data)

    elif request.method == 'POST':
        #jsonData = JSONParser().parse(request)
        #serializer = EmployeeSerializer(data = jsonData )
        serializer = EmployeeSerializer(data = request.data )
        if serializer.is_valid():
            serializer.save()
            #return JsonResponse(serializer.data,safe = False)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


#@csrf_exempt  
@api_view(['GET','PUT','DELETE'])
def employeeDetailsViews(request,pk):
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        # return Response(serializer.data , safe=False)
        return Response(serializer.data )

    if request.method == 'PUT':
        #jsonData = JSONParser().parse(request)
        #serializer = EmployeeSerializer(employee, data = jsonData )
        serializer = EmployeeSerializer(employee, data = request.data)
        if serializer.is_valid():
            serializer.save()
            #return Response(serializer.data,safe = False)
            return Response(serializer.data)
        else:
            return Response(serializer.errors) 
 
    if request.method == 'DELETE':
        employee.delete()
        #return JsonResponse(status.HTTP_204_NO_CONTENT , safe=False)
        return Response(status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def userListViews(request):
    if request.method=='GET':
        users = User.objects.all()
        # serializer = UserSerializer(users , many = True)
        # return JsonResponse(serializer.data , safe=False) 
        serializer = UserSerializer(users ,many = True
        
        
        )
        return Response(serializer.data ) 