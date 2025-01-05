from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Testimonial(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the user
    content = models.TextField()  # Testimonial content
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the creation date
    approved = models.BooleanField(default=False)  # Admin approval status

    class Meta:
        ordering = ['-created_at']  # Order by newest first

    def __str__(self):
        return f"Testimonial by {self.user.username}"
