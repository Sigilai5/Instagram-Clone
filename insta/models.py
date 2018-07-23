from django.db import models

from tinymce.models import HTMLField


from django.contrib.auth.models import User

# Create your models here.


class Comments(models.Model):
    comment = models.CharField(max_length=30,default='Comment')

class Image(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    post_image = models.ImageField(upload_to='post/',default='card')
    image_caption = models.CharField(max_length=30,null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    comments = models.ForeignKey(Comments,null=True)


    def __str__(self):
        return self.owner
    class Meta:
        ordering = ['owner']









