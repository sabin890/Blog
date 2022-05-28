from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("",views.index),
    path("Blog/", views.home, name='Blog'),
    path("about/", views.About,name='about'),
    path("contact/", views.contact,name='contact'),
    path("signup/", views.signup,name='signup'),
    path("login/", views.log_in,name='login'),
    path("User/", views.user,name='User'),
    path("logout/", views.log_out,name='logout'),
    path("blog/", views.blog_post,name='blog'),
    path("blogupdate/<int:id>/", views.blog_update,name='blogupdate'),
    path("delete/<int:id>/", views.delete,name='delete'),
    path("update/<int:id>/",views.update,name='update'),
    path("profile/",views.profile,name='profile'),
    path("blogdetails/<int:id>/",views.blogdetails,name='blogdetails'),
    ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
