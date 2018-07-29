from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200,help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email','password1','password2')

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['owner']

        # widgets = {
        #     ''
        # }


class CommentForm(forms.ModelForm):
    comment = forms.CharField(label='Comment', max_length=30)

    class Meta:
        model = Comments
        exclude =['image','by']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude =['user']



class LikeForm(forms.ModelForm):
    class Meta:
        model = Like
        exclude = ['timestamp','post','user','total_likes']