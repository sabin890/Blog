from django.db import models


# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField()
    photo=models.ImageField(upload_to="image")
    date=models.DateTimeField(auto_now_add=True)

class Port(models.Model):
    title=models.CharField(max_length=200)
    sabin=models.ImageField(upload_to="image")
    date=models.DateTimeField(auto_now_add=True)
