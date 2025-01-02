from django.db import models
from django.utils.timezone import now

class Testimonial(models.Model):
    name = models.CharField(max_length=100)  # User's name
    email = models.EmailField()  # User's email
    content = models.TextField()  # Testimonial content
    created_on = models.DateTimeField(default=now)  # Creation date
    approved = models.BooleanField(default=False)  # Admin approval status

    def __str__(self):
        return f"Testimonial by {self.name}"
