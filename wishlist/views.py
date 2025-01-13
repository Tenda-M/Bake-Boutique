from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product
from .models import Wishlist
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect

# credit: https://www.youtube.com/watch?v=OgA0TTKAtqQ
@login_required
def add_to_wishlist(request, product_id):
    # Get the product from the database
    product = Product.objects.get(id=product_id)

    # Check if the product is already in the user's wishlist
    if not Wishlist.objects.filter(user=request.user, product=product).exists():
        Wishlist.objects.create(user=request.user, product=product)
        message = f"{product.name} has been added to your wishlist."
        success = True
    else:
        message = f"{product.name} is already in your wishlist."
        success = False

    # Check if the request is AJAX using the correct header
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'message': message, 'success': success})

    # If not AJAX, use Django messages framework to send a message and redirect
    messages.info(request, message)
    return redirect('products:product_detail', product_id=product.id)


@login_required
def remove_from_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist_item = get_object_or_404(Wishlist, user=request.user, product=product)
    wishlist_item.delete()
    messages.success(request, f"{product.name} has been removed from your wishlist.")
    return redirect('wishlist:view_wishlist')

@login_required
def view_wishlist(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist/view_wishlist.html', {'wishlist_items': wishlist_items})

