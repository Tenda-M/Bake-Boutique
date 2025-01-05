from django.urls import path
from . import views

urlpatterns = [
    path('', views.testimonial_list, name='testimonial_list'),
    path('add/', views.add_testimonial, name='add_testimonial'),
    path('edit/<int:id>/', views.edit_testimonial, name='edit_testimonial'),
    path('delete/<int:id>/', views.delete_testimonial, name='delete_testimonial'),
]
