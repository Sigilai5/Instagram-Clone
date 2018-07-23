from .models import *
from django import forms


class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['owner']

        # widgets = {
        #     ''
        # }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude =['image','by']

    comment = forms.CharField(label='Comment', max_length=30)


