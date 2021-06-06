
from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'cart'
urlpatterns = [
    path('shopping_list', TemplateView.as_view(template_name='cart/shopping_list.html'), name='shopping_list'),
    path('cart', views.cart, name='cart'),
    path('cart_list', TemplateView.as_view(template_name = 'cart/cart_list.html'), name='cart_list'),
    path('order', views.order, name='order'),
]
