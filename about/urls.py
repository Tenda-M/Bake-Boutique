from django.urls import path
from . import views

app_name = 'about'

urlpatterns = [
    path('', views.about_us, name='about_us'),
]

