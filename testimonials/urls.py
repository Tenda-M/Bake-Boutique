from django.urls import path
from . import views

urlpatterns = [
    path('', views.testimonial_list, name='testimonial_list'),
    path('submit/', views.submit_testimonial, name='submit_testimonial'),
    path('add/', views.add_testimonial, name='add_testimonial'),
]
