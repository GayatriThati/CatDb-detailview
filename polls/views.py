from django.shortcuts import render

# Create your views here.
from .models import Home,Human,Breed,Cat

def home(request):
    home1 = Home()
    home1.name = 'Home1'
    home1.address = 'address1'
    home1.house_type = 'landed'
    
    home2 = Home()
    home2.name = 'Home2'
    home2.address = 'address2'
    home2.house_type = 'condominium'
    
    #@Homes = Home.objects.all()
    homes = [home1,home2]
    context = {'homes' : homes }
    return render(request,'polls/home.html',context)

def human(request):
    human1 = Human()
    human1.name = 'Human1'
    human1.gender = 'Female'
    human1.date_of_birth = '3rd March, 1996'
    human1.description = 'Brown and Beautiful!'
    human1.home = 1
    
    human2 = Human()
    human2.name = 'Human2'
    human2.gender = 'Male'
    human2.date_of_birth = '5th Nov, 1992'
    human2.description = 'Tall and Handsome!'
    human2.home = 1
    
    humans = [human1,human2]
    context = {'humans' : humans }
    return render(request,'polls/human.html',context)

def breed(request):
    
    breed1 = Breed()
    breed1.name = 'American Bobtail'
    breed1.origin = 'Mutation'
    breed1.description = 'Cobby'
        
    breed2 = Breed()
    breed2.name = 'Brazilian Shorthair'
    breed2.origin = 'Natural'
    breed2.description = 'Normal'
    
    breeds = [breed1,breed2]
    context = {'breeds' : breeds }
    return render(request,'polls/breed.html',context)

def cat(request):
    cat1 = Cat()
    cat1.name = 'Cat1'
    cat1.gender = 'Male'
    cat1.date_of_birth = '1st Jan,2010'
    cat1.description = 'Cute and soft'
    cat1.breed = 'Cyprus'
    cat1.owner = 'Human1'
    
    cat2 = Cat()
    cat2.name = 'Cat2'
    cat2.gender = 'Male'
    cat2.date_of_birth = '15th Aug,2015'
    cat2.description = 'fluffy'
    cat2.breed = 'Foldex'
    cat2.owner = 'Human2'
    
    cats = [cat1,cat2]
    context = {'cats' : cats }
    return render(request,'polls/cat.html',context)


















