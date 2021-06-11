from django.urls import path
from . import views

urlpatterns = [
    path('get_greeting', views.get_greeting, name='get_greeting'),
    path('get_item_by_id', views.get_item_by_id, name='get_item_by_id'),
    path('get_item_list', views.get_item_list, name='get_item_list'),
]