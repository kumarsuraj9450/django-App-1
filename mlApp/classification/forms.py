from django import forms

from .models import image_file

# class IMAGE_UPLOAD_FORM(forms.ModelForm):
#     class Meta:
#             model  = image_file
#             fields = [
#                 'image',
#                 'url',
#             ]

class IMAGE_UPLOAD_FORM(forms.Form):
    image = forms.ImageField()
    url   = forms.URLField()
        