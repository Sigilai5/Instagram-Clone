from .models import *
from django import forms


class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['owner','comment']

        # widgets = {
        #     ''
        # }


class CommentForm(forms.Form):
    model = Comments
    exclude = ['image']

    comment = forms.CharField(label='Comment', max_length=30)

