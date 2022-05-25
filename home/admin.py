from django.contrib import admin
from .models import Blog, Contact, Port
# Register your models here.
@admin.register(Blog)
class BlogModelAdmin(admin.ModelAdmin):
    list_display =['id','title','body','photo','date']

@admin.register(Port)
class PortModelAdmin(admin.ModelAdmin):
    list_display =['id','title','sabin','date']

@admin.register(Contact)
class contactModelAdmin(admin.ModelAdmin):
    list_display =['id','name','email','address','massage']
