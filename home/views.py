from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import Photo, SignUp,Post,Cont,Log
from .models import Blog, Port
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import  User
# blogs.


def home(request):
    std = Blog.objects.all()
    return render(request, "home/home.html", {"bb": std})
# home


def index(request):
    std = User.objects.all()
    return render(request, "home/index.html", {"name": request.user, "fm": std})
# About.


def About(request):
    return render(request, "home/about.html")

# Sign Up


def signup(request):
    if request.method == "POST":
        fm = SignUp(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect("login")
    else:
        fm = SignUp()
    return render(request, "home/signup.html", {"form": fm})

# Contact.


def contact(request):
    if request.method == "POST":
        fm=Cont(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect("contact")
    else:
        fm=Cont()
        return render(request, "home/contact.html",{"bm":fm})

# log in


def log_in(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = Log(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    return render(request, "home/index.html",{'name': request.user})
                   
        else:
            fm = Log()
        return render(request, "home/log.html", {"form": fm})
    else:
        return HttpResponseRedirect("/Blog/")
# user


@login_required(login_url="login")
def user(request):
    std = Port.objects.all()
    for sd in std:
        if str(request.user) == str(sd.title):
            st=sd
            return render(request, "home/prof.html", {"ph":st,"name":request.user})
    
    return render(request, "home/prof.html", {"ph":"No-Profile","name":request.user})
    

# logout


def log_out(request):
    logout(request)
    return HttpResponseRedirect("/login/")

# blog


@login_required(login_url="login")
def blog_post(request):
    if request.method == "POST":
        fm = Post(request.POST or None, request.FILES)
        if fm.is_valid():
            fm.save()
        fm = Post()
    else:
        fm = Post()
    return render(request, "home/blogpost.html", {"form": fm})

# blog update


@login_required(login_url="login")
def blog_update(request, id):
    if request.method == 'POST':
        ak = Blog.objects.get(pk=id)
        pm = Post(request.POST or None, files=request.FILES, instance=ak)
        if pm.is_valid():
            pm.save()
            messages.success(request, "Blog Successfully updated!!!")
        return HttpResponseRedirect("/Blog/")
    else:
        ak = Blog.objects.get(pk=id)
        pm = Post(instance=ak)
    return render(request, "home/blogupdate.html", {'pp': pm})

# deleate


def delete(request, id):
    if request.user.is_superuser == True:
        sk = Blog.objects.get(pk=id)
        sk.delete()
        return redirect("Blog")
    else:
        messages.error(request, "You cant Use this feature!!!")
        return redirect("Blog")


def update(request,id):
    if request.method == 'POST':
        ak = Port.objects.get(pk=id)
        pm = Photo(request.POST or None, files=request.FILES, instance=ak)
        if pm.is_valid():
            pm.save()
            messages.success(request, "Blog Successfully updated!!!")
            return redirect("User")
    else:
        ak =Port.objects.get(pk=id)
        pm = Photo(instance=ak)
    return render(request, "home/update.html", {'pp': pm})

def profile(request):
    if request.method == "POST":
        fm = Photo(request.POST or None, request.FILES)
        if fm.is_valid():
            fm.save()
            return redirect('User')
    else:
        fm = Photo()
    return render(request,"home/profile.html",{"form":fm})


def blogdetails(request,id):
    post=Blog.objects.get(pk=id)
    return render(request,"home/blogdetails.html",{"post":post})
    