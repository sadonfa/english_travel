from django.db import models

# Create your models here.

class Travels(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(default="null", upload_to="Travels")
    create_ad = models.DateTimeField(auto_now_add=True)
    update_ad = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.title}'