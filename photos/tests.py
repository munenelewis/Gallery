from django.test import TestCase
from .models import Image,Location,Category

class ImageTest(TestCase):

    def setUp(self):

        self.img3 = Image(name= 'image3', description = 'the guys')

    def test_instance(self):
        self.assertTrue(isinstance(self.img3, Image))
    #