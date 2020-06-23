"""CatDB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from catwiki.views import HomeDetail,IndexList,HumanDetail
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', IndexList.as_view()), 
    path('home/<pk>/', HomeDetail.as_view()),
    #url(r'^(?P<home_slug>[\w-]+)$', HomeDetail.as_view()),
    path('human/<pk>/', HumanDetail.as_view()),
    
]



