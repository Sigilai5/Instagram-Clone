from django.db import models
<<<<<<< HEAD
from tinymce.models import HTMLField
=======
>>>>>>> 58ba2ff16d14163795c0afe9d1d6e9871230f806
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    image_name = models.CharField(max_length=30)
<<<<<<< HEAD
    post = HTMLField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    post_image = models.ImageField(upload_to='post/',default='card')
=======
    image_caption = models.CharField(max_length=30)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,default='Brian')
    post_image = models.ImageField(upload_to='post/', default='card')
>>>>>>> 58ba2ff16d14163795c0afe9d1d6e9871230f806

    def __str__(self):
        return self.image_name
    class Meta:
        ordering = ['image_name']