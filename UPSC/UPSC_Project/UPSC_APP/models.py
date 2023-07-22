from django.db import models

# Create your models here.
class Data(models.Model):
    country=models.CharField(max_length=100000)
    capital=models.CharField(max_length=100000)
    union=models.CharField(max_length=100000)
    river=models.CharField(max_length=100000)
    fest_day=models.CharField(max_length=100000)
    border_countrie=models.CharField(max_length=100000)
    population=models.CharField(max_length=100000)
    current_prime_minister=models.CharField(max_length=100000)