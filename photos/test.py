from django.test import TestCase
from .models import Image,Location,Category

class ImageTest(TestCase):

    def setUp(self):

        self.img3 = Image(name= 'image3', description = 'the guys')
        
    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.img3, Image))
    #testing for saving images

    def test_save_imge(self):
        self.img3.save_image()
        image = Image.objects.all()
        self.assertTrue(len(image)> 0)

    def test_delete(self):
        self.img3.save_image()
        image = Image.objects.all()
        self.img3.delete_image()
        self.assertTrue(len(image) < 1)
    def test_get_image_by_location(self):
        test_location = 'nairobi'
    
        self.assertTrue(len(image)> 0 )
    

