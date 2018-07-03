from rest_framework import serializers
from .models import Pizza, Topping

class PizzaSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='pizzadetails', read_only=True)

    class Meta:
        model = Pizza
        fields = ('url','id', 'name', 'price')


class ToppingSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='toppingdetails', read_only=True)
    class Meta:
        model = Topping
        fields = ('url', 'id', 'name', 'veg', 'stock')



class PizzaTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = ('id', 'is_veg')
