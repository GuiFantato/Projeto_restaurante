from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from django.shortcuts import render

from kitchen.models import Dish, DishType, Cook
from kitchen.forms import DishForm

# Create your views here.

class DishesListView(ListView):
    model = Dish
    template_name = 'dishes_list.html'
    paginate_by = 5


class DishesCreateView(CreateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("kitchen:dishes-list")


class DishesUpdateView(CreateView):
    model = Dish
    form_class = DishForm
    template_name = 'dish_form.html'
    success_url = reverse_lazy("kitchen:dishes-list")


class DishesDeleteView(CreateView):
    model = Dish
    template_name = 'dish_confirm_delete.html'
    success_url = reverse_lazy("kitchen:dishes-list")


class DishesDetailView(DetailView):
    model = Dish
    template_name = 'kitchen/dish_detail.html'


class DishTypeListView(ListView):
    model = DishType
    template_name = 'dish_type_list.html'
    paginate_by = 5


class CookListView(ListView):
    model = Cook
    template_name = 'cook_list.html'
    paginate_by = 5
