from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product
from .models import Wishlist
from django.http import JsonResponse

@login_required
def add_to_wishlist(request, product_id):
    # Get the product from the database
    product = Product.objects.get(id=product_id)

    # Check if the product is already in the user's wishlist
    if not Wishlist.objects.filter(user=request.user, product=product).exists():
        Wishlist.objects.create(user=request.user, product=product)
        # Add success message
        message = f"{product.name} has been added to your wishlist."
        success = True
    else:
        # Add message if the product is already in the wishlist
        message = f"{product.name} is already in your wishlist."
        success = False

    # If the request is AJAX, return a JsonResponse
    if request.is_ajax():
        return JsonResponse({'message': message, 'success': success})

    # If not AJAX, redirect to the product detail page
    return redirect('products:product_detail', product_id=product.id)



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

