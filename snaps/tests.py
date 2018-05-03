from django.test import TestCase
from .models import Image,Location,Category
# Create your tests here.
class ImageTestClass(TestCase):
    def setUp(self):
        self.location = Location(location = 'dubai')
        self.location.save()
        self.category = Category(category = 'travel')
        self.category.save()
        self.new_image=Image(image_link = 'snaps/img.png',name = 'car',description = 'An exclusive picture of the limited edition range rover velar',location= self.location,category=self.category)
        self.new_image.save()
    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))
    def test_save_method(self):
        self.new_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)
