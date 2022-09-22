from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
import re
from django.contrib.auth.decorators import login_required
from django.conf import settings
import requests
# import requests
def recaptcha_check(response):
    data = data={'secret':settings.RECAPTCHA_SECRET_KEY,'response': response}
    response_json = requests.post('https://www.google.com/recaptcha/api/siteverify',data=data).json()
    return True if response_json.get('success') else False


def login(request):
    if request.method == 'POST':
        #LOGIN
        if 'loginbtn' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            recaptcharesponse = request.POST.get('g-recaptcha-response')

            if settings.RECAPTCHA_LOGIN:
                if recaptcha_check(recaptcharesponse):
                    pass
                else :
                    messages.error(request,'Recaptcha error')
                    return render(request,'login.html')


            if username and password:
                user = auth.authenticate(username=username,password=password)
                if user is not None:
                    if "rememberme" not in request.POST:
                        request.session.set_expiry(0)
                    auth.login(request,user)
                    return redirect('home')
                else :
                    messages.error(request,'Incorrect Username or password')  
            else :
                messages.error(request,'Check Empty Fields')


        #Signup
        elif 'signupbtn' in request.POST:
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            recaptcharesponse = request.POST.get('g-recaptcha-response')

            if settings.RECAPTCHA_SIGNUP:
                if recaptcha_check(recaptcharesponse):
                    pass
                else :
                    messages.error(request,'Recaptcha Error')
                    return render(request,'login.html')

            if first_name and last_name and re.match(r'''^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$''',email) and username and password:
                if not User.objects.filter(username=username).exists():
                    if not User.objects.filter(email=email).exists():
                        user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
                        user.save()
                        messages.success(request,"Account is Created")
                    else:
                        messages.error(request,'Email is taken')
                else :
                    messages.error(request,'Username is taken')
            else :
                messages.error(request,'Check Empty Fields')

            
    
    return render(request,'login.html',{
        "recaptcha_site_key" : settings.RECAPTCHA_SITE_KEY,
        "loginrecaptcha": settings.RECAPTCHA_LOGIN,
        "signuprecaptcha": settings.RECAPTCHA_SIGNUP,
    })

@login_required
def logout(request):
    auth.logout(request)
    return redirect('home')
