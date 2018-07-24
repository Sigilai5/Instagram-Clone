from django.db import models

from tinymce.models import HTMLField


from django.contrib.auth.models import User

# Create your models here.





class Image(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    post_image = models.ImageField(upload_to='post/',default='card')
    image_caption = models.CharField(max_length=30,null=True)
    # comment = models.CharField(max_length=30, default='Comment',blank=True)



    def __str__(self):
        return self.image_caption
    class Meta:
        ordering = ['owner']

class Comments(models.Model):
    comment = models.TextField(default='Tri')
    image = models.ForeignKey(Image, related_name='comment')
    by = models.ForeignKey(User,related_name='by',null=True)


class Profile(models.Model):
    pic = models.ImageField(upload_to='profile/',default='prof')
    bio = HTMLField()
    user = models.ForeignKey(User,related_name='user',null=True)







