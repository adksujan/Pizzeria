from django.shortcuts import render
from api.models import Pizza, Topping
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django.http import Http404
from api.serializers import PizzaSerializer, ToppingSerializer, PizzaTypeSerializer, MenuSerializer, AddToppingsSerializer


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


class PizzaMenu(generics.ListAPIView):
    """
    Shows all pizza details with Toppings
    """
    queryset = Pizza.objects.all()
    serializer_class = MenuSerializer


class AddToppings(generics.UpdateAPIView):
    """
    Add toppings to pizza using array of Topping ids api/addtoppings/<pizza_id>
    """
    queryset = Pizza.objects.all()
    serializer_class = AddToppingsSerializer
