from django.db import models

class ContactUsForm(models.Model):
    """
    Stores a single contact us request message
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Contact from {self.name}"
