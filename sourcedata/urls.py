from django.urls import path
from . import views


app_name = 'sourcedata'
urlpatterns = [
    path('', views.inventory_list, name='inventory_list'),
    
]