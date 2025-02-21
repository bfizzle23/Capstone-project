from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics, viewsets, permissions

# Create your views here.
class MenuItemView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = menuItemSerializer
    
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = menuItemSerializer
    
class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer