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

    def is_veg(self):
        """
        checks if the pizza is veg or not
        """
        for x in self.toppings.all():
            if not x.veg :
                return False
        return True
        # return all([x.veg for x in self.toppings])
