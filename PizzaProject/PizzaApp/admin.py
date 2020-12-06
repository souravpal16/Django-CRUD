from django.contrib import admin
from .models import PizzaModel, Toppings, Sizes
# Register your models here.
admin.site.register(PizzaModel)
admin.site.register(Toppings)
admin.site.register(Sizes)