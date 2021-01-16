from django.db import models
from django.db.models import Manager
# Create your models here.


class UserManager(models.Manager):
    pass


class CreateEmployee(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    re_password = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    Designation = models.CharField(max_length=100, default='', blank=True)

    def __str__(self):
        return self.username
