from django.shortcuts import render

# Create your views here.

def about_us(request):
    return render(request, 'about/about_us.html', {'page_title': 'About Us'})
