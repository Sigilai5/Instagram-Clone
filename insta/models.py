from django.db import models

from tinymce.models import HTMLField


from django.contrib.auth.models import User


# Create your models here.





class Image(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    post_image = models.ImageField(upload_to='post/',default='card')
    image_caption = models.CharField(max_length=30,null=True)
    # image_date = models.DateTimeField(auto_now_add=True,null=True)
    # comment = models.CharField(max_length=30, default='Comment',blank=True)

    def save_image(self):
        self.save()

    def __str__(self):
        return self.image_caption
    class Meta:
        ordering = ['owner']

    @classmethod
    def filter_user(cls,user):
        images = cls.objects.filter(owner__username__icontains=user)
        return images

class Comments(models.Model):
    comment = models.TextField(default='Tri')
    image = models.ForeignKey(Image, related_name='comment')
    by = models.ForeignKey(User,related_name='by',null=True)
    # comment_date = models.DateTimeField(auto_now_add=True,null=True)


class Like(models.Model):
    user = models.ForeignKey(User,related_name='us',null=True)
    post = models.ForeignKey(User,related_name='post',null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    total_likes = models.IntegerField(default=0)

class Profile(models.Model):
    pic = models.ImageField(upload_to='profile/',default='prof')
    bio = HTMLField()
    user = models.OneToOneField(User,related_name='profile',null=True)
    profile_date = models.DateTimeField(auto_now_add=True,null=True)

    @classmethod
    def search_users(cls,search_user):
        users = cls.objects.filter(user__username__icontains=search_user)
        return users





