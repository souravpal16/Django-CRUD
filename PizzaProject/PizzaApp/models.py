from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Toppings(models.Model):
    topp = models.CharField(max_length=20)

class Sizes(models.Model):
    size = models.CharField(max_length=20)


class PizzaModel(models.Model):
    type_choices = (
        ('REGULAR', 'Regular'),
        ('SQUARE', 'Square')
    )

    type_of_pizza = models.CharField(max_length=7, choices= type_choices)
    size = models.CharField(max_length=20)
    toppings = ArrayField(models.CharField(max_length = 15))








