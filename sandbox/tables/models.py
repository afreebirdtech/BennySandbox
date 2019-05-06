from django.db import models
from django.conf import settings
from phone_field import PhoneField
# Create your models here.

class Usertype(models.Model):
    name = models.CharField(max_length=128)
    def __str__(self):
        return self.name


class User(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(blank=True, unique=True)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    
    def __str__(self):
        return self.first_name

class Program(models.Model):
    name = models.CharField(max_length=128)
