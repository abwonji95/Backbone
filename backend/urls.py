from collections import namedtuple
from django.urls import path,include
from  . import views
from .views import *
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[

#home
    path('home',views.home,name='home'),
    path('',views.test,name='test'),
    ]