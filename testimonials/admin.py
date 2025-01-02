from django.contrib import admin
from .models import Testimonial

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'approved', 'created_on')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'content')
    actions = ['approve_testimonials']

    def approve_testimonials(self, request, queryset):
        queryset.update(approved=True)
    approve_testimonials.short_description = "Approve selected testimonials"
