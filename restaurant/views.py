from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Menu, Booking
from django.contrib.auth.models import User
from .serializers import MenuSerializer, UserSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated


# Create your views here.
from django.http import HttpResponse

def sayHello(request):
 return HttpResponse('Hello World')


def index(request):
    return render(request, 'index.html', {})

class MenuItemsView (generics.ListCreateAPIView):
   queryset = Menu.objects.all()
   serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class Users (generics.ListCreateAPIView):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [IsAuthenticated]

class BookView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class SingleBookView(generics.RetrieveUpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer