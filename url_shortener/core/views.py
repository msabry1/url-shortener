from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Url
from django.contrib import messages
import random



def get_path(num):
    path = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890",k=num))
    try :
        if  Url.objects.filter(shortenurl=path) or path.lower() in ['accounts','admin']:
            return get_path(num)
        else :
            return path
    except RecursionError:
        return get_path(num+1)


def url(request):
    if request.method == 'POST':
        try : # to get lenth of char of shortenurl to can guess
            num = len(Url.objects.last())
        except :
            num = 1


        url = request.POST.get('urlpath')
        originalurl =  url if url.startswith('http://') or url.startswith('https://') else f"http://{url}"
        password = request.POST.get('password')

        if originalurl and 'btn-submit' in request.POST :
                    instance = Url(user=request.user if request.user.is_authenticated else None,originalurl=originalurl,shortenurl=get_path(num),password=password)
                    instance.save()
                    return render(request,'index.html',{
                        'shorturl':request.build_absolute_uri(instance.shortenurl),
                        "urls":Url.objects.filter(user=request.user if request.user.is_authenticated else None)
                    })
    else:
        return render(request,'index.html',{"urls":Url.objects.filter(user=request.user if request.user.is_authenticated else None)})
    


def urldetail(request,short_str):
    url = Url.objects.filter(shortenurl=short_str)
    if url.exists():
        url = Url.objects.get(shortenurl=short_str)
        if url.password:
            return redirect(f'/{url.shortenurl}/password')
        else :
            url.urlviews += 1
            url.save()
            return redirect(url.originalurl)
    else :
        return render(request,'404.html',status=404)



def urlpassword(request,short_str):
    if request.method == 'POST':
        password = request.POST.get('password')
        if password and 'password-btn' in request.POST:
            url_object = Url.objects.get(shortenurl=short_str)
            if url_object.password == password:
                url_object.urlviews += 1
                url_object.save()
                return redirect(request.build_absolute_uri(url_object.originalurl))
            else :
                messages.error(request,'Incorrect Password')
        else :
            messages.error(request,'Check Empty Values')
    
    return render(request,'password.html')
