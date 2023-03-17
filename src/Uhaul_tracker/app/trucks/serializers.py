from rest_framework import serializers
from trucks.models import Truck, Location 

class truckserializers(serializers.ModelSerializer): 
    class Meta: 
        model = Truck
        fields = ('id', 'rented', 'locations', 'users') 

class locationserializers(serializers.ModelSerializer): 
    class Meta: 
        model = Location
        fields = ('id', 'state', 'city')