from django.db import models

class Topping(models.Model):
    name = models.CharField(max_length=100)
    veg = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Pizza(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    toppings = models.ManyToManyField(Topping)

    def __str__(self):
        return self.name
