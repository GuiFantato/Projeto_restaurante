from django.views.generic import ListView
from django.shortcuts import render

from kitchen.models import Dish

# Create your views here.

class DishesListView(ListView):
    model = Dish
    template_name = 'dishes_list.html'
    paginate_by = 5


