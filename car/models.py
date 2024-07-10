from django.db import models
from brand.models import BrandModel
# Create your models here.
class CarModel(models.Model):
    img = models.ImageField(upload_to=('images/'))
    name = models.CharField(max_length=255)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.CharField(max_length=255)
    
    brand = models.ForeignKey(BrandModel,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Comment(models.Model):
    name = models.CharField(max_length=30, blank=True , null= True)
    email = models.EmailField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    car = models.ForeignKey(CarModel,on_delete=models.CASCADE, related_name='comments',blank=True,null = True) 
    
    
    def __str__(self):
        return f"Commented by {self.name}"
class Order(models.Model):
    carId = models.IntegerField()
    userId = models.IntegerField()
    
    def __str__(self):
        return f"carid {self.carId} oreder by userid {self.userId}"