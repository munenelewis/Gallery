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
    image_url = models.ImageField(upload_to = 'images/',  null=True)


    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()
    
    def __str__(self):
        return self.name
    @classmethod
    def get_image(cls, location):
        photos = cls.objects.filter(location = location)
        return photos
    @classmethod
    def search_category(cls, search_term) :
        photos = cls.objects.filter(category__icontains=search_term)
        return photos
    @property
    def photo_url(self):
        if self.image_url and hasattr(self.image_url, 'url'):
            return self.image_url.url