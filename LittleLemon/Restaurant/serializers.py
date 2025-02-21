from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url','username','email','groups']
        
class menuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = "__all__"
        
class bookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"