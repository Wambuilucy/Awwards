from django import forms
from . models import  *

class ProjectUpload(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','image','description','link')

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']