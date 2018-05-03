from django.test import TestCase
from .models import Image,Location,Category
# Create your tests here.
class ImageTestClass(TestCase):
    def setUp(self):
        self.location = Location(location_name = 'dubai')
        self.location.save()
        self.category = Category(category_name = 'travel')
        self.category.save()
        self.new_image=Image(image_link = 'snaps/img.png',name = 'car',description = 'An exclusive picture of the limited edition range rover velar',location= self.location,category=self.category)
        self.new_image.save()
    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))
    def test_save_method(self):
        self.new_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)
    def test_delete_method(self):
        self.new_image.save_image()
        images = Image.objects.all()
        self.new_image.delete_image()
        self.assertTrue(len(images)==0)
    def test_update_method(self):
        self.new_image.save_image()
        self.new_image.update_image(self.new_image.id,'snaps/img1.png')
        image = Image.objects.filter(image_link= 'snaps/img1.png').all()
        self.assertTrue(len(image)==1)
    def test_get_image_by_id(self):
        find_img = self.new_image.get_image_by_id(self.new_image.id)
        img = Image.objects.filter(id = self.new_image.id)
        self.assertTrue(find_img,img)
    def test_search_image_by_category(self):
        find_img = self.new_image.search_by_cate('travel')
        self.assertTrue(len(find_img)==1)
