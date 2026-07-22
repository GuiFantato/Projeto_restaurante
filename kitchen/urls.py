from django.contrib import admin
from django.urls import include, path
from .views import DishesListView

urlpatterns = [
    path('dishes/', DishesListView.as_view(), name='dishes-list'),
]
