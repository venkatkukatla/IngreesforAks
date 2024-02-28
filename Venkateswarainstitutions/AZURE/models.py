from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=1000)
    fathername = models.CharField(max_length=1000)
    contact = models.CharField(max_length=1000)
   

# class Onlinetraining(models.Model):
#     Azure = models.CharField(max_length=1000)
#     AWS = models.CharField(max_length=1000)
#     Azuredevops = models.CharField(max_length=1000)
#     Jenkins = models.CharField(max_length=1000)