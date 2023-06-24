from django.db import models
class Movie(models.Model):
    rdate=models.DateField()
    moviename=models.CharField(max_length=50)
    hero=models.CharField(max_length=50)
    heroine=models.CharField(max_length=50)
    rating=models.IntegerField()
# Create your models here.
