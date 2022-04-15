from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Blog, Port

class SignUp(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']

class Post(forms.ModelForm):
    class Meta:
        model=Blog
        fields=['id','title','body','photo']


class Photo(forms.ModelForm):
    class Meta:
        model=Port
        fields=['id','sabin','title']
        