from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Terms(models.Model):
    term = models.CharField(max_length = 100)
    definition = models.CharField(max_length = 100)
    image = models.URLField(max_length = 10000, null = True, blank = True)
    set = models.IntegerField(default=None, null=True)

class Set(models.Model):
    title = models.CharField(max_length = 50)
    owner = models.CharField(max_length = 20, null=True)
    description = models.CharField(max_length = 100)
