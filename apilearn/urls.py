from django.contrib import admin
from django.urls import path,include
from rest_framework.serializers import Serializer
from app.views import employeeListViews , userListViews ,employeeDetailsViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/employees', employeeListViews),
    path('api/employees/<int:pk>', employeeDetailsViews),
    path('api/users', userListViews)
]
