from django import forms
from django.core.validators import MaxLengthValidator
from .models import Testimonial

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'content']

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) > 100:
            raise forms.ValidationError("Your testimonial exceeds the 100-character limit.")
        return content