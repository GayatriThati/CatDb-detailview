from django.db import models

# Create your models here.
class Home(models.Model):
    name =  models.CharField(max_length = 200,default =True)
    adress = models.TextField(default = True)
    house_type = models.CharField(max_length = 200,default =True)

class Human(models.Model):
    name =  models.CharField(max_length = 200,default =True)
    gender = models.CharField(max_length = 200,default =True)
    #date_of_birth = models.DateTimeField('date published') 
    date_of_birth = models.CharField(max_length = 200,default =True)
    description = models.TextField(default = True)
    home  = models.IntegerField(default = True)
    
class Breed(models.Model):
    name =  models.CharField(max_length = 200,default =True)
    origin = models.TextField(default = True)
    description = models.TextField(default = True)

class Cat(models.Model):
    name =  models.CharField(max_length = 200,default =True)
    gender = models.CharField(max_length = 200,default =True)
    #date_of_birth = models.DateTimeField('date published') 
    date_of_birth = models.CharField(max_length = 200,default =True)
    description = models.TextField(default = True)
    breed = models.CharField(max_length = 200,default =True)
    owner = models.CharField(max_length = 200,default =True)
 