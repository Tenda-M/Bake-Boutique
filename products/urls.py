from django.urls import path
from . import views

app_name = 'products'  # Ensure that the app_name is set to 'product'

urlpatterns = [
    path('', views.all_products, name='products'), #'products' URL
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'), # This is the URL for adding a product 
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('<int:product_id>/add_review/', views.add_review, name='add_review'),
    path('review/<int:review_id>/edit/', views.edit_review, name='edit_review'),
    path('review/<int:review_id>/delete/', views.delete_review, name='delete_review'),

]
