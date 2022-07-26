from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=64)
    body = models.CharField()
    date_published = models.DateField()