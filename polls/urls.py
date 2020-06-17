# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 15:58:34 2020

@author: GVN
"""
from django.urls import path 
from . import views

urlpatterns = [
        path('home/',views.home,name = 'home'),
        path('human/',views.human,name = 'human'),
        path('breed/',views.breed,name = 'breed'),
        path('cat/',views.cat,name = 'cat'),
        ]