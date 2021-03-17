from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Set(models.Model):
    title = models.CharField(max_length = 50)
    owner = models.CharField(max_length = 20, null=True)
    term = models.CharField(max_length = 50)
    description = models.CharField(max_length = 100)
    image = models.URLField(max_length = 1000)