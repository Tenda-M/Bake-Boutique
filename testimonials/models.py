from django.db import models
from django.utils.timezone import now

class Testimonial(models.Model):
    name = models.CharField(max_length=255)  # User's name
    content = models.TextField()  # Testimonial content
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the creation date
    approved = models.BooleanField(default=False)  # Admin approval status

    class Meta:
        ordering = ['-created_at']  # Order by newest first

    def __str__(self):
        return f"Testimonial by {self.name}"


