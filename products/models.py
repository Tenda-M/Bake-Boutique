from django.db import models

from django.contrib.auth.models import User


# Create your models here.
"""     name: Holds the category's name (e.g., "Cakes", "Cupcakes", "Cookies").
    friendly_name: Provides a user-friendly name for display purposes.
    The get_friendly_name method allows easy access to the friendly name in templates or logic.

Product Model:

    category: A foreign key to the Category model, linking each product to a specific category.
    sku: Stores a stock-keeping unit, a unique identifier for each product.
    name: Stores the product's name (e.g., "Red Velvet Cake").
    description: A detailed description of the product.
    price: The price of the product, using DecimalField for accuracy in monetary values.
    rating: A nullable rating field for customer reviews or ratings.
    image_url and image: Options to use either a URL or an uploaded image for product pictures."""

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

################### Review #############
# Credit : https://www.youtube.com/watch?v=UgEVC7oJDHI
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Review by {self.user.username}"


