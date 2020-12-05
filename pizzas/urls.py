from django.urls import path
from . import views

app_name = 'pizzas'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('pizzas', views.pizzas, name = 'pizzas'),
    path('toppings/<int:pizza_id>/', views.toppings, name='toppings'),
    path('comments/', views.comments, name = 'comments')
]