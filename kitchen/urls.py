from django.contrib import admin
from django.urls import include, path
from .views import DishesDeleteView, DishesListView, DishesCreateView, DishesDetailView, DishesUpdateView
from .views import DishTypeListView, DishTypeCreateView, DishTypeDetailView, DishTypeUpdateView, DishTypeDeleteView
from .views import CookListView, CookDeleteView, CookDetailView, CookUpdateView, CookCreateView

urlpatterns = [
    path('dishes/', DishesListView.as_view(), name='dish-list'),
    path('dishes/create/', DishesCreateView.as_view(), name='dish-create'),
    path('dishes/<int:pk>/', DishesDetailView.as_view(), name='dish-detail'),
    path('dishes/<int:pk>/update/', DishesUpdateView.as_view(), name='dish-update'),
    path('dishes/<int:pk>/delete/', DishesDeleteView.as_view(), name='dish-delete'),
    path('dish-type/', DishTypeListView.as_view(), name='dish-type-list'),
    path('dish-type/create/', DishTypeCreateView.as_view(), name='dish-type-create'),
    path('dish-type/<int:pk>/', DishTypeDetailView.as_view(), name='dish-type-detail'),
    path('dish-type/<int:pk>/update/', DishTypeUpdateView.as_view(), name='dish-type-update'),
    path('dish-type/<int:pk>/delete/', DishTypeDeleteView.as_view(), name='dish-type-delete'),
    path('cooks/', CookListView.as_view(), name='cook-list'),
    path('cooks/create/', CookCreateView.as_view(), name='cook-create'),
    path('cooks/<int:pk>/', CookDetailView.as_view(), name='cook-detail'),
    path('cooks/<int:pk>/update/', CookUpdateView.as_view(), name='cook-update'),
    path('cooks/<int:pk>/delete/', CookDeleteView.as_view(), name='cook-delete'),
]

app_name = "kitchen"