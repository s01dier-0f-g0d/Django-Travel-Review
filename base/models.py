from django.db import models 

class Destination(models.Model): 
    name = models.CharField(max_length=100) 
    country = models.CharField(max_length=100) 
    description = models.CharField(max_length=500) 
    average_cost = models.IntegerField() 
    rating = models.IntegerField()  # 1-5 scale 
    image = models.ImageField(upload_to='destination_images/', blank=True, null=True)

def __str__(self): 
    return self.name 