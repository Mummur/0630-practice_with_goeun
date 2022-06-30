from django.db import models

# Create your models here.

class Poll(models.Model):
    name = models.CharField(max_length=32)
    gender = models.CharField(max_length=4)
    home = models.CharField(max_length=8)
    home_suggest = models.TextField()