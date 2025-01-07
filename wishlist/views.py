from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Wishlist
from products.models import Product

# Create your views here.
@login_required
def add_to_wishlist(request, product_id):
    product = Product.objects.get(id=product_id)
    if not Wishlist.objects.filter(user=request.user, product=product).exists():
        Wishlist.objects.create(user=request.user, product=product)
    return redirect('wishlist:view_wishlist')

@login_required
def remove_from_wishlist(request, product_id):
    product = Product.objects.get(id=product_id)
    wishlist_item = Wishlist.objects.get(user=request.user, product=product)
    wishlist_item.delete()
    return redirect('wishlist:view_wishlist')

@login_required
def view_wishlist(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist/view_wishlist.html', {'wishlist_items': wishlist_items})

