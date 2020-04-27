from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=256)
    desc = models.CharField(max_length=256)
    year = models.CharField(max_length=256)