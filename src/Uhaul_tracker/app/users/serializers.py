from rest_framework import serializers
from users.models import User 

class userserializers(serializers.ModelSerializer): 
    class Meta: 
        model = User
        fields = ('first_name', 'last_name', 'phone_number', 'email', 'password') 