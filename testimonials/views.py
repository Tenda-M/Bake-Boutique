from django.shortcuts import render, redirect
from .forms import TestimonialForm
from .models import Testimonial


def testimonial_list(request):
    testimonials = Testimonial.objects.filter(approved=True)  # Only show approved testimonials
    return render(request, 'testimonials/testimonial_list.html', {'testimonials': testimonials})

def add_testimonial(request):
    if request.method == "POST":
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("testimonial_list") # Redirect to the testimonials list
    else:
        form = TestimonialForm()
    return render(request, "testimonials/testimonial_form.html", {"form": form, "page_title": "Add Testimonial"})

def submit_testimonial(request):
    if request.method == "POST":
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("testimonial_list") # Redirect to the testimonials list
    else:
        form = TestimonialForm()
    return render(request, "testimonials/testimonial_form.html", {"form": form, "page_title": "Submit Your Testimonial"})
