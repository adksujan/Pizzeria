from rest_framework import serializers
from .models import Pizza, Topping

class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = ('id', 'name', 'price')


class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = ('id', 'name', 'veg')



class PizzaTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = ('id', 'is_veg')
