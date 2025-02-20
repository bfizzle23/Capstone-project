from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics, viewsets, permissions

# Create your views here.
class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = menuItemSerializer
    
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.RetrieveDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = menuItemSerializer
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer
    #permission_classes = [permissions.IsAuthenticated]