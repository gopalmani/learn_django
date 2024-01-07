# from django.db import models

# Create your models here.

from django.db import models

class User(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  joined_date = models.DateField(null=True)
  phone = models.IntegerField(null=True)

# class Member(models.Model):
#   firstname = models.CharField(max_length=255)
#   lastname = models.CharField(max_length=255)



