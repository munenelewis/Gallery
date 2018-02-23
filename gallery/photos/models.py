from django.db import models

# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length = 30)
    def __str__(self):
            return self.location
class Category(models.Model):
    category = models.CharField(max_length = 30)
    def __str__(self):
            return self.category
class Image(models.Model):
    name = models.CharField(max_length = 30)
    description = models.CharField(max_length = 100)
    location = models.ForeignKey(Location, blank=True, null=True)
    category = models.ForeignKey(Category, blank=True, null=True)

    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()
    
    def __str__(self):
        return self.name

