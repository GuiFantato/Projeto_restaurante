from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.shortcuts import render

from kitchen.models import Dish, DishType, Cook
from kitchen.forms import DishForm

# Create your views here.

class DishesListView(ListView):
    model = Dish
    template_name = 'dish_list.html'
    paginate_by = 5


class DishesCreateView(CreateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("kitchen:dish-list")


class DishesUpdateView(UpdateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("kitchen:dish-list")


class DishesDeleteView(DeleteView):
    model = Dish
    success_url = reverse_lazy("kitchen:dish-list")


class DishesDetailView(DetailView):
    model = Dish
    template_name = 'kitchen/dish_detail.html'


class DishTypeListView(ListView):
    model = DishType
    template_name = 'kitchen/dish_type_list.html'
    paginate_by = 5


class DishTypeCreateView(CreateView):
    model = DishType
    template_name = 'kitchen/dish_type_form.html'
    fields = ['name']
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishTypeDetailView(DetailView):
    model = DishType
    template_name = "kitchen/dish_type_detail.html"


class DishTypeUpdateView(UpdateView):
    model = DishType
    template_name = 'kitchen/dish_type_form.html'
    fields = ['name']
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishTypeDeleteView(DeleteView):
    model = DishType
    template_name = 'kitchen/dish_type_confirm_delete.html'
    success_url = reverse_lazy("kitchen:dish-type-list")


class CookListView(ListView):
    model = Cook
    template_name = 'cook_list.html'
    paginate_by = 5
