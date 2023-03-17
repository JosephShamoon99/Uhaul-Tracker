from rest_framework.decorators import api_view  
from rest_framework.response import Response
from users.models import User
from users.serializers import userserializers


# Create your views here. 

@api_view(['POST']) 
def add_user(request): 
    serializer = userserializers(data=request.data) 
    if serializer.is_valid(): 
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE']) 
def remove_user(request, user_id):  
   user = User.objects.get(pk=user_id) 
   user.delete()  
   return Response('Account deleted')