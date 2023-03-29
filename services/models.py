from django.db import models

# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to="Services")
    create_ad = models.DateTimeField(auto_now_add=True)
    update_ad = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"