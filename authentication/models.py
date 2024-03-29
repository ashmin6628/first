from pyexpat import model
from unicodedata import category, name
from django.db import models
from .category import Category
from .customer import Customer


# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=100 , null= False)
    email= models.EmailField(max_length=100)
    message= models.TextField(max_length=1000)

    def __str__(self):
        return self.name


class RestaurentRegister(models.Model):
    name= models.CharField(max_length=100)
    address= models.CharField(max_length=100)
    contact= models.IntegerField()

    def __str__(self):
        return self.name

#############

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category , on_delete=models.CASCADE , default=1)
    description = models.CharField(max_length=500, default='')
    image = models.ImageField(upload_to='uploads/products/')

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in = ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products();


##################



  

    


