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


class MenuSerializer(serializers.ModelSerializer):
    toppings = serializers.SerializerMethodField(source='get_toppings')
    def get_toppings(self,obj):
        return [x.name for x in obj.toppings.all()]
    class Meta:
        model = Pizza
        fields = ('name', 'price', 'is_veg', 'toppings')
