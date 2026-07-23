from django.urls import reverse_lazy
from django.views.generic import ListView
from django.shortcuts import render

from kitchen.models import Dish, DishType, Cook

# Create your views here.

class DishesListView(ListView):
    model = Dish
    template_name = 'dishes_list.html'
    paginate_by = 5


class DishTypeListView(ListView):
    model = DishType
    template_name = 'dish_type_list.html'
    paginate_by = 5


class CookListView(ListView):
    model = Cook
    template_name = 'cook_list.html'
    paginate_by = 5
