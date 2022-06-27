from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import FoodSerializer
from .models import Food

class FoodList(generics.ListCreateAPIView):
    queryset = Food.objects.all().order_by('id')