from django.db import models

class ProductCategory(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Product(models.Model):
    product_category=models.ForeignKey('ProductCategory',on_delete=models.CASCADE)
    product_name=models.CharField(max_length=25)
    product_description=models.TextField()
    product_price=models.DecimalField(decimal_places=5,max_digits=10)
    product_availablity=models.BooleanField()
    product_discount=models.DecimalField(decimal_places=5,max_digits=10)

    def __str__(self):
        return self.product_name
