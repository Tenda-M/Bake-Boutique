"""bake_boutique URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from .views import handler404
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site
    path('accounts/', include('allauth.urls')),  # django-allauth handles all account views
    path('', include('home.urls')),  # Home app URLs
    path('products/', include('products.urls')),  # Products app URLs
    path('bag/', include('bag.urls')),  # Bag app URLs
    path('checkout/', include('checkout.urls')),  # Checkout app URLs
    path('profile/', include('profiles.urls')),  # Profiles app URLs
    path('testimonials/', include('testimonials.urls')),  # Testimonials app URLs
    path('wishlist/', include('wishlist.urls')), # wishlist
    path('about/', include('about.urls')),
    path('contact/', include('contact.urls', namespace='contact')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'bake_boutique.views.handler404'
handler403 = 'bake_boutique.views.handler403'
handler405 = 'bake_boutique.views.handler405'
handler500 = 'bake_boutique.views.handler500'

