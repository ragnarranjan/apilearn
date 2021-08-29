from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField

class Employee(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    phone = models.IntegerField()

    def __str__(self):
        return self.name



