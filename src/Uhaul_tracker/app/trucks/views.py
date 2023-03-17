from rest_framework.decorators import api_view  
from rest_framework.response import Response
from trucks.models import Location, Truck, User
from trucks.serializers import truckserializers, locationserializers 
from users.serializers import userserializers


# Create your views here.

@api_view(['GET']) 
def trucks_by_location(request, locations_id):  
    trucks = Truck.objects.filter(locations=locations_id).filter(rented= False) 
    serializer = truckserializers(trucks, many=True)
    return Response(serializer.data) 

@api_view(['POST']) 
def rent(request,truck_id):   
    truck = Truck.objects.get(pk=truck_id)   
    serializer = truckserializers(instance=truck, data=request.data)
    if serializer.is_valid(): 
        serializer.save()
    return Response(serializer.data)
     
@api_view(['POST']) 
def return_truck(request,truck_id):   
    truck = Truck.objects.get(pk=truck_id)   
    serializer = truckserializers(instance=truck, data=request.data)
    if serializer.is_valid(): 
        serializer.save()
    return Response(serializer.data)
   
