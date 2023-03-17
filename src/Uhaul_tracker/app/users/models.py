from django.db import models

# Create your models here. 
class User(models.Model): 
    first_name = models.CharField(max_length=30) 
    last_name = models.CharField(max_length=30) 
    phone_number = models.IntegerField() 
    email = models.EmailField() 
    password = models.CharField(max_length=30) 



