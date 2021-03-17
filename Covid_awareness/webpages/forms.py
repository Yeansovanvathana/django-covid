from django import forms
from .models import ProfileImage

class ImageForm(forms.ModelForm):
    class Meta:
        model=ProfileImage
        fields=("image",)