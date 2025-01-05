from django.shortcuts import render, redirect
from .forms import TestimonialForm
from .models import Testimonial
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def testimonial_list(request):
    testimonials_list = Testimonial.objects.filter(approved=True)  # Only approved testimonials
    paginator = Paginator(testimonials_list, 6)  # 6 testimonials per page
    page_number = request.GET.get('page')  # Get the current page number from the query string
    testimonials = paginator.get_page(page_number)  # Get the relevant page of testimonials
    testimonials = Testimonial.objects.filter(approved=True).order_by('-created_at')


    # Pass the paginated testimonials to the template
    return render(request, 'testimonials/testimonial_list.html', {
        'testimonials': testimonials
    })

@login_required
def add_testimonial(request):
    if request.method == "POST":
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("testimonial_list")  # Redirect to the testimonials list
    else:
        form = TestimonialForm()
    return render(request, "testimonials/testimonial_form.html", {"form": form, "page_title": "Add Testimonial"})

