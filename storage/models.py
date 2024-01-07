from django.db import models

# Create your models here.
class Product(models.Model):
    sno=models.AutoField(primary_key=True)
    title_string=models.TextField()
    mrp=models.TextField()
    discountedPrice=models.TextField()
    rating=models.TextField()
    review_count=models.TextField()
    available=models.TextField()
    ram=models.TextField()
    os=models.TextField()
    modelName=models.TextField()
    importer=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)
    def save(self):
        super(Product,self).save()
        
    def __str__(self):
        return self.title_string+ ' | '+self.ram