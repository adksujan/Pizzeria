from django.shortcuts import render
from api.models import Pizza, Topping
from api.serializers import PizzaSerializer, ToppingSerializer, PizzaTypeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


class PizzaList(APIView):
    """
    List all Pizza
    """
    def get(self, request, format=None):
        pizzas = Pizza.objects.all()
        serializer = PizzaSerializer(pizzas, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PizzaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PizzaDetails(APIView):
    """
    Details of a Pizza
    """
    def get_object(self, pk):
        try:
            return Pizza.objects.get(pk=pk)
        except Pizza.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        pizza = self.get_object(pk)
        serializer = PizzaSerializer(pizza)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        pizza = self.get_object(pk)
        serializer = PizzaSerializer(pizza, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        pizza = self.get_object(pk)
        pizza.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ToppingsList(APIView):
    """
    List all Toppings
    """
    def get(self, request, format=None):
        topping = Topping.objects.all()
        serializer = ToppingSerializer(topping, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ToppingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ToppingDetails(APIView):
    """
    Details of a Topping
    """
    def get_object(self, pk):
        try:
            return Topping.objects.get(pk=pk)
        except Topping.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        topping = self.get_object(pk)
        serializer = ToppingSerializer(topping)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        topping = self.get_object(pk)
        serializer = ToppingSerializer(topping, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        topping = self.get_object(pk)
        topping.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PizzaType(APIView):
        """
        Tells if the Pizza is vegeterian  with a given id
        """
        def get_object(self, pk):
            try:
                return Pizza.objects.get(pk=pk)
            except Pizza.DoesNotExist:
                raise Http404

        def get(self, request, pk, format=None):
            topping = self.get_object(pk)
            serializer = PizzaTypeSerializer(topping)
            return Response(serializer.data)
