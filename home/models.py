
from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=500)
    body=models.TextField()
    photo=CloudinaryField("image")
    date=models.DateTimeField(auto_now_add=True)

class Port(models.Model):
    title=models.CharField(max_length=200)
    sabin=CloudinaryField("image")
    date=models.DateTimeField(auto_now_add=True)
    write_about_you=models.TextField()

class Contact(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    address=models.CharField(max_length=30)
    massage=models.TextField(max_length=500)