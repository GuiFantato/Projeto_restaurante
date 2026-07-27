from django.contrib import admin
from django.urls import include, path
from .views import DishesListView, DishesCreateView, DishesDetailView, DishTypeListView, CookListView

urlpatterns = [
    path('dishes/', DishesListView.as_view(), name='dishes-list'),
    path('dishes/create/', DishesCreateView.as_view(), name='dish-create'),
    path('dishes/<int:pk>/', DishesDetailView.as_view(), name='dish-detail'),
    path('dish-types/', DishTypeListView.as_view(), name='dish-types-list'),
    path('cooks/', CookListView.as_view(), name='cooks-list'),
]

app_name = "kitchen"