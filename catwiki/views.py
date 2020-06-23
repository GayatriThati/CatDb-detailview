from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Home,Human,Breed, Cat
from django.urls import reverse


# Create your views here.
class IndexList(ListView):
    
    template_name = 'catwiki/index.html'
    
    def get_queryset(self):
        return Home.objects.all()

    def get_queryset(self):
        return Human.objects.all()

class HomeDetail(DetailView):
    
    model = Home
    template_name = 'catwiki/home_detail.html'

class HumanDetail(DetailView):
    
    model = Human
    template_name = 'catwiki/human_detail.html'

    