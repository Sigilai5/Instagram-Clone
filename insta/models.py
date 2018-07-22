from django.db import models

# Create your models here.
class Image(models.Model):
    image_name = models.CharField(max_length=30)
    image_caption = models.CharField(max_length=30)
    owner = models.CharField(max_length=20,default='Sigila')
    post_image = models.ImageField(upload_to='post/',default='card')

    def __str__(self):
        return self.image_name
    class Meta:
        ordering = ['image_name']