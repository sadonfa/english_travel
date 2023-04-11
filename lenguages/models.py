from django.db import models
from ckeditor.fields import RichTextField 

# Create your models here.

class Lenguages(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(default="null", upload_to="Lenguage")
    content = RichTextField(verbose_name="Contenido")
    create_ad = models.DateTimeField(auto_now_add=True)
    update_ad = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.title}'