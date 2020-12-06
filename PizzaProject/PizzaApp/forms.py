from .models import PizzaModel
from django import forms

class PizzaModelForm(forms.ModelForm):
    class Meta:
        model = PizzaModel
        fields = ('type_of_pizza','size','toppings' )

        



