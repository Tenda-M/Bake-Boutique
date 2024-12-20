from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51QY64aJzMFHkUexIHDGpe6Wz4n6wF1oTTQeSOe85CC1JPCAQa6WutlGdfdCBZqCb98JKxilRY1a7WYNTIjh75uHt00Fc07gOT6',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)