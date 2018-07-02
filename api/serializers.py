from rest_framework import serializers
from .models import Pizza, Topping

Class PizzaSerializer(serializers.ModelSerializer):
    Class Meta:
        model = Pizza
        fields = ('id', 'name', 'price')


Class ToppingSerializer(serializers.ModelSerializer):
    Class Meta:
        model = Topping
        fields = ('id', 'name', 'veg')
