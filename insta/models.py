from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    image_name = models.CharField(max_length=30)
    image_caption = models.CharField(max_length=30)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,default='Brian')
    post_image = models.ImageField(upload_to='post/', default='card')

    def __str__(self):
        return self.image_name
    class Meta:
        ordering = ['image_name']