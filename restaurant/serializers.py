from rest_framework import serializers
from .models import Booking, Menu
from rest_framework import serializers
from django.contrib.auth.models import User

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'title', 'price', 'author', 'inventory']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['name', 'no_of_guests', 'booking_date']




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'groups']

