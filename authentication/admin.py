from unicodedata import category
from django.contrib import admin

# Register your models here.
from .models import Contact
from .models import RestaurentRegister
from .models import Product
from .category import Category
from .customer import Customer
from .orders import Orders


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Contact)
admin.site.register(RestaurentRegister)
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer)
admin.site.register(Orders)





