from django.db import models

# Create your models here.
class Item(models.Model): # models.model is inherited
    item_name = models.CharField(max_length=200, blank=False)   # item memory space
    item_desc = models.CharField(max_length=200, blank=False)   # description of the item
    item_price = models.IntegerField(blank=False)               # price of the item

    '''using database abstraction API to create objects in the DB'''
    ''''''