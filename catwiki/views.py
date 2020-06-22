from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Home,Human,Breed, Cat

# Create your views here.
class IndexList(ListView):
    template_name = 'catwiki/index.html'
    
    def get_queryset(self):
        return Home.objects.all()
'''        
class HumanList(ListView):
    model = Human
class BreedList(ListView):
    model = Breed
class CatList(ListView):
    model = Cat
'''
class HomeDetail(DetailView):
    model = Home
    template_name = 'catwiki/home_detail.html'
    