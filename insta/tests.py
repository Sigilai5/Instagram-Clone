from django.test import TestCase
from .models import *
# Create your tests here.


class ImageTestClass(TestCase):

    def setUp(self):
        self.can = Image(owner='Brian',post_image='image.jpg',image_caption='Nothing')


    def test_instance(self):
        self.assertTrue(isinstance(self.can,Image))

    def test_save_method(self):
        self.can.save_image()
        loc = Image.objects.all()
        self.assertTrue(len(loc)>0)
