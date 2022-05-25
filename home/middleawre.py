# from django.shortcuts import render,HttpResponse

from django.shortcuts import render


class Fathermymiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        print(" father One time initialization")


    def __call__(self,request):
        print("Father Befor view")
        response=render(request,'home/up.html')
        return response
    
        
