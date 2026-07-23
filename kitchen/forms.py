from django import forms
from django.contrib.auth.forms import UserCreationForm
from kitchen.models import Dish


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = (
            "name",
            "description",
            "price",
            "dish_type",
            "cooks"
        )
