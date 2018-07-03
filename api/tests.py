from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Pizza, Topping
import json

# Create your tests hereself.
class PizzaTests(APITestCase):
    """
    Test for Pizzas
    """

    def test_create_pizza(self):
        """
        Make sure we can create pizza object
        """
        url = reverse('pizza')
        data = {'name': 'Tonno', 'price':"2.99"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Pizza.objects.count(), 1)
        self.assertEqual(Pizza.objects.get().name, 'Tonno')

    def test_get_pizza(self):
        pizza = Pizza.objects.create(name="Tonno", price="2.99")
        url = reverse("pizza")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(json.loads(response.content)) == Pizza.objects.count())

    def test_update_pizza(self):
        """
        Ensure update is done
        """
        pizza = Pizza.objects.create(name="Tonno", price="2.99")
        url = reverse("pizzadetails", kwargs={"pk": pizza.pk})
        data = {'name': 'Pollo', 'price':"2.99"}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content).get('name'), data.get('name'))

    def test_delete_pizza(self):
        """
        Ensure we can delete pizza object
        """
        pizza = Pizza.objects.create(name="Tonno", price="2.99")
        url = reverse("pizzadetails", kwargs={"pk": pizza.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Pizza.objects.count(), 0)

class ToppingTests(APITestCase):
    """
    Test for Topping
    """

    def test_create_topping(self):
        """
        Make sure we can create topping object
        """
        url = reverse('topping')
        data = {'name': 'spinat', 'veg':'true', 'stock':'5.0'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Topping.objects.count(), 1)
        self.assertEqual(Topping.objects.get().name, 'spinat')

    def test_get_toppings(self):
        """
        Make sure we get list of topping objects
        """
        topp = Topping.objects.create(name="spinat", veg=True)
        url = reverse('topping')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(json.loads(response.content)) == Topping.objects.count())

    def test_update_topping(self):
        """
        Ensure update is done
        """
        topp = Topping.objects.create(name="spinat", veg=True)
        url = reverse("toppingdetails", kwargs={"pk": topp.pk})
        data = {'name': 'rotpaprika', 'veg':'true'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content).get('name'), data.get('name'))

    def test_delete_topping(self):
        """
        Ensure we can delete topping object
        """
        topp = Topping.objects.create(name="spinat", veg=True)
        url = reverse("toppingdetails", kwargs={"pk": topp.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Topping.objects.count(), 0)

class PizzaTypeTest(APITestCase):
    def test_vegeterian(self):
        """
        Check if the pizza type is correct according to the topping PizzaType
        """
        pizza = Pizza.objects.create(name="Veg Pizza", price="0.99")
        spinat = Topping.objects.create(name="spinat", veg=True)
        paprika = Topping.objects.create(name="paprika", veg=True)
        pizza.toppings.add(spinat)
        pizza.toppings.add(paprika)
        url = reverse("pizzatype", kwargs={"pk": pizza.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content).get('is_veg'), True)
        chicken = Topping.objects.create(name="chicken", veg=False)
        pizza.toppings.add(chicken)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content).get('is_veg'), False)
