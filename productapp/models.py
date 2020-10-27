from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)
    logourl = models.ImageField(max_length=255,upload_to='logos/%Y/%m/%d/', null=True, blank=True)
    active = models.BooleanField(default=True)

class Product(models.Model):
    description = models.CharField(max_length=500)
    imageurl = models.ImageField(max_length=255,upload_to='images/%Y/%m/%d/', null=True, blank=True)
    price = models.FloatField()
    reorderqty = models.IntegerField()
    stockavailable = models.IntegerField()
    brandid = models.ForeignKey(Brand,on_delete=models.CASCADE, related_name='prods')
    active = models.BooleanField(default=True)
