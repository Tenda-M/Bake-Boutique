from django.urls import path
from . import views

app_name = 'bag'  # This defines the namespace for the app

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    #path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
    path('add/<int:item_id>/', views.add_to_bag, name='add_to_bag'),  # New pattern
    path('add/<int:product_id>/', views.add_to_bag, name='add_to_bag'),  # Old pattern
    path('adjust/<item_id>/', views.adjust_bag, name='adjust_bag'),
    path('remove/<item_id>/', views.remove_from_bag, name='remove_from_bag'),
]