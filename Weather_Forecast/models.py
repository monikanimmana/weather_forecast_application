from django.db import models

# Create your models here.
class Weather_Details(models.Model):
    city=models.TextField()

    def __str__(self):
        return self.city
