from django.shortcuts import render
from api.models import Pizza, Topping
from api.serializers import PizzaSerializer, ToppingSerializer, PizzaTypeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django.http import Http404


class PizzaList(generics.ListCreateAPIView):
    """
    List all Pizza
    """
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer

class PizzaDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Details of a Pizza
    """
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer

class ToppingsList(generics.ListCreateAPIView):
    """
    List all Toppings
    """
    queryset = Topping.objects.all()
    serializer_class = ToppingSerializer


class ToppingDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Details of a Topping
    """
    queryset = Topping.objects.all()
    serializer_class = ToppingSerializer

class PizzaType(generics.RetrieveAPIView):
    """
    Tells if the Pizza is vegeterian  with a given id
    """
    queryset = Pizza.objects.all()
    serializer_class = PizzaTypeSerializer
