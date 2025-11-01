from django.db import models 

class Country(models.Model):
    name = models.CharField(max_length=30)
    desc = models.CharField(max_length=500)
    image = models.ImageField(upload_to='country_images/', blank=True, null=True)

    def __str__(self):
        return self.name


class Destination(models.Model): 
    name = models.CharField(max_length=100) 
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='destination') 
    description = models.CharField(max_length=500) 
    average_cost = models.PositiveIntegerField() 
    rating = models.IntegerField(range(1,6))  # 1-5 scale 
    image = models.ImageField(upload_to='destination_images/', blank=True, null=True)
    video = models.FileField(upload_to='destination_videos/', null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


def __str__(self): 
    return self.name 