from rest_framework import serializers
from .models import Pizza, Topping


class ToppingSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='toppingdetails', read_only=True)
    class Meta:
        model = Topping
        fields = ('url', 'id', 'name', 'veg', 'stock')


class ToppingSerializer2(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Topping
        fields = ["id"]


class PizzaSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='pizzadetails', read_only=True)
    class Meta:
        model = Pizza
        fields = ('url','id', 'name', 'price')


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

class ToppingOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = ['id']


class AddToppingsSerializer(serializers.ModelSerializer):
    add_by_id = serializers.BooleanField(default=True)
    # topping = ToppingOptionSerializer()
    class Meta:
        model = Pizza
        fields = ['id','add_by_id','toppings']
        # read_only_fields = ['name']


    def update(self, instance, validated_data):
        """
        updates the toppings in a pizza by new array of topping ids, removes all the old toppings
        """
        if(validated_data.pop("add_by_id")):
            try:
                # topping = validated_data.pop("topping")
                topping_ids = validated_data.pop("toppings")
                print(topping_ids)
                toppings = instance.toppings
                instance.toppings.clear()
                for t in topping_ids:
                    instance.toppings.add(t)
                instance.save()
            except serializers.ValidationError:
                return
        else:
            # todo.. still to implement
            return instance
        return instance
