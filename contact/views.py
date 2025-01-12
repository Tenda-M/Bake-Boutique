from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact:contact_success')# Redirect to success page
    else:
        form = ContactForm()  # Render empty form for GET request

    return render(request, 'contact/contact.html', {'form': form})


def contact_success(request):
    """
    Displays a success message after form submission.
    """
    return render(request, 'contact/contact_success.html')

   

