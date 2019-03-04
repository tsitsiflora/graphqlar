from django.db import models

# Create your models here.
class User(models.Model):
    username = models.TextField()
    name = models.TextField(blank=False)
    password = models.TextField(blank=False)
class Trip(models.Model):
    driver_name = models.TextField(blank=False)
    reg_number = models.TextField(blank=False)
    opening_milage = models.IntegerField()
    closing_milage = models.IntegerField()
    destination = models.TextField(blank=False)
    comments = models.TextField()
    date = models.DateField()
