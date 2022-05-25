from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import Blog, Contact, Port

class SignUp(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible_field in self.visible_fields():
            visible_field.field.widget.attrs['class']='form-control'

class Post(forms.ModelForm):
    class Meta:
        model=Blog
        fields=['id','title','photo','body']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible_field in self.visible_fields():
            visible_field.field.widget.attrs['class']='form-control'


class Photo(forms.ModelForm):
    class Meta:
        model=Port
        fields=['id','sabin','title','write_about_you']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible_field in self.visible_fields():
            visible_field.field.widget.attrs['class']='form-control'

class Cont(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['id','name','email','address','massage']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible_field in self.visible_fields():
            visible_field.field.widget.attrs['class']='form-control'

class Log(AuthenticationForm):
    
     def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible_field in self.visible_fields():
            visible_field.field.widget.attrs['class']='form-control'
