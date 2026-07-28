from django.contrib import admin
from django.urls import include, path
from .views import DishesDeleteView, DishesListView, DishesCreateView, DishesDetailView, DishTypeListView, CookListView, DishesUpdateView

urlpatterns = [
    path('dishes/', DishesListView.as_view(), name='dishes-list'),
    path('dishes/create/', DishesCreateView.as_view(), name='dish-create'),
    path('dishes/<int:pk>/', DishesDetailView.as_view(), name='dish-detail'),
    path('dishes/<int:pk>/update/', DishesUpdateView.as_view(), name='dish-update'),
    path('dishes/<int:pk>/delete/', DishesDeleteView.as_view(), name='dish-delete'),
    path('dish-types/', DishTypeListView.as_view(), name='dish-types-list'),
    path('cooks/', CookListView.as_view(), name='cooks-list'),
]

app_name = "kitchen"