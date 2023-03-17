from django.db import models  
from users.models import User

# Create your models here.
class Location(models.Model): 
    state = models.CharField(max_length=30)  
    city = models.CharField(max_length=30)   

class Truck(models.Model): 
    rented = models.BooleanField(default=False)
    locations = models.ForeignKey(Location, on_delete=models.CASCADE, null=True) 
    users = models.ForeignKey(User, on_delete=models.CASCADE, null=True)











