from django.db import models

# Create your models here.
class Image(models.Model):
    image_link = models.ImageField(upload_to ='snaps/')
    name = models.CharField(max_length = 100)
    description = models.TextField()
    location = models.ForeignKey('Location',null = True)
    category = models.ForeignKey('Category', null =True)

    def save_image(self):
        self.save()
    def delete_image(self):
        self.delete()
    @classmethod
    def update_image(cls,id,link):
        cls.objects.filter(id = id).update(image_link=link)
    @classmethod
    def get_image_by_id(cls,id):
        imge = cls.objects.filter(id =id).all()
        return imge
class Location(models.Model):
    location = models.CharField(max_length = 60)
class Category(models.Model):
    category = models.CharField(max_length = 60)
