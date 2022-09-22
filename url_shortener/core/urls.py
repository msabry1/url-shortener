from django.urls import path 
from . import views

urlpatterns = [ 
    path('',views.url,name='home'),
    path('<str:short_str>/',views.urldetail,name='short_redirect'),
    path('<str:short_str>/password/',views.urlpassword,name='password_url'),
]