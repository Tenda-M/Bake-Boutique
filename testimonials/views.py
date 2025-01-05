from django.shortcuts import render, redirect, get_object_or_404
from .forms import TestimonialForm
from .models import Testimonial
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def testimonial_list(request):
    # Only fetch approved testimonials
    testimonials_list = Testimonial.objects.filter(approved=True).order_by('-created_at')
    paginator = Paginator(testimonials_list, 6)  # 6 testimonials per page
    page_number = request.GET.get('page')  # Get the current page number from the query string
    testimonials = paginator.get_page(page_number)  # Get the relevant page of testimonials

    # Pass the paginated testimonials to the template
    return render(request, 'testimonials/testimonial_list.html', {
        'testimonials': testimonials
    })


@login_required
def add_testimonial(request):
    if request.method == "POST":
        form = TestimonialForm(request.POST)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.user = request.user  # Link testimonial to the logged-in user
            testimonial.save()
            return redirect("testimonial_list")  # Redirect to the testimonials list
    else:
        form = TestimonialForm()
    return render(request, "testimonials/testimonial_form.html", {"form": form, "page_title": "Add Testimonial"})


@login_required
def edit_testimonial(request, id):
    # Ensure the testimonial belongs to the logged-in user
    testimonial = get_object_or_404(Testimonial, id=id, user=request.user)
    if request.method == 'POST':
        form = TestimonialForm(request.POST, instance=testimonial)
        if form.is_valid():
            form.save()
            return redirect('testimonial_list')
    else:
        form = TestimonialForm(instance=testimonial)
    return render(request, 'testimonials/testimonial_form.html', {'form': form, 'page_title': 'Edit Testimonial'})


@login_required
def delete_testimonial(request, id):
    # Ensure the testimonial belongs to the logged-in user
    testimonial = get_object_or_404(Testimonial, id=id, user=request.user)
    if request.method == 'POST':
        testimonial.delete()
        return redirect('testimonial_list')
    return render(request, 'testimonials/confirm_delete.html', {'testimonial': testimonial})
