from django.db import models

from tinymce.models import HTMLField


from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    post_image = models.ImageField(upload_to='post/',default='card')
    image_caption = models.CharField(max_length=30)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,default='Brian')


    def __str__(self):
        return self.owner
    class Meta:
        ordering = ['owner']



