from __future__ import unicode_literals

from django.db import models


# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    cinta = models.CharField(max_length=30, blank=True)
    fecha_ingreso = models.DateField(null=True, blank=True)