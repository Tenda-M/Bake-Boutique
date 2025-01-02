from django.shortcuts import render, redirect
from .forms import TestimonialForm
from .models import Testimonial

def testimonial_list(request):
    testimonials = Testimonial.objects.filter(approved=True).order_by('-created_on')
    return render(request, 'testimonials/testimonial_list.html', {'testimonials': testimonials})

def submit_testimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('testimonial_list')  # Redirect after submission
    else:
        form = TestimonialForm()
    return render(request, 'testimonials/submit_testimonial.html', {'form': form})
