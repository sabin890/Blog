from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from django.dispatch import receiver
@receiver(user_logged_in,sender=User)
def user_log(sender,request,user,**kwargs ):
    ip=request.META.get('REMOTE_ADDR')
    request.session['ip']=ip
    