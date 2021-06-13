from django.db import models


# Create your models here.

class Country(models.Model):
    name= models.CharField(max_length= 100)

    def __str__(self):
        return f'{self.name}'

class Category(models.Model):
    name= models.CharField(max_length= 200)

    def __str__(self):
        return f'{self.name}'

class Director(models.Model):
    first_name= models.CharField(max_length= 100)
    last_name= models.CharField(max_length= 100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Film(models.Model):
    title= models.CharField(max_length= 300)
    release_date= models.DateTimeField(auto_now_add=True)
    created_in_country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name ='created_in_country')
    available_in_countries= models.ManyToManyField(Country)
    category= models.ManyToManyField(Category)
    director= models.ManyToManyField(Director)
    emp_image = models.ImageField(upload_to='upload/', null=True, blank=True)

    def __str__(self):
        return f'{self.title}'




