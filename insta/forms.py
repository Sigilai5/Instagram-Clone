from .models import Image
from django import forms


class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['owner']
        # widgets = {
        #     ''
        # }


class CommentForm(forms.Form):
    comment = forms.CharField(label='Comment', max_length=30)
