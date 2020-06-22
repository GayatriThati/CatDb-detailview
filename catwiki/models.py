from django.db import models

# Create your models here.
class Home(models.Model):

    LANDED = 'Landed'
    CONDOMINIUM = 'Condominium'
    HOUSE_TYPE_CHOICES = [
            (LANDED, 'Landed'),
            (CONDOMINIUM,'Condominium'),
    ]
    name = models.CharField(max_length=200, primary_key=True)
    address = models.TextField(blank=True)
    house_type = models.CharField(max_length=100, choices=HOUSE_TYPE_CHOICES, default=LANDED)

    def __str__(self):
        return self.name

class Human(models.Model):

    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = [
            (MALE, 'M'),
            (FEMALE, 'F'),
    ]
    name = models.CharField(max_length=200, primary_key=True)
    gender = models.CharField(max_length=200, choices=GENDER_CHOICES, default=None)
    date_of_birth = models.DateField(blank=True, null=True) 
    description = models.TextField()
    home = models.ForeignKey('Home', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Breed(models.Model):

    name = models.CharField(max_length=200, primary_key=True)
    origin = models.TextField()
    description = models.TextField()
    
    def __str__(self):
        return self.name

class Cat(models.Model):

    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = [
            (MALE, 'M'),
            (FEMALE, 'F'),
    ]
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=200, choices=GENDER_CHOICES, default=None)
    date_of_birth = models.DateField(blank=True, null=True) 
    description = models.TextField()
    breed = models.ForeignKey('Breed', on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey('Human', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
        
