from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length = 30)
    description = models.CharField(max_length = 100)
    location = models.ForeignKey(Location)
    category = moels.ForeignKey(Category)
    def __str__(self):
        return self.name
class Location(models.Model):
    location = models.CharField(max_length = 30)

class Category(models.Model):
    category = models.CharField(max_length = 30)

