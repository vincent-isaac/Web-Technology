from django.shortcuts import render

# Create your views here.

def home(request):
    context = {}
    return render(request, 'design/home.html', context)

def product(request):
    context = {}
    return render(request, 'design/product.html', context)

def people(request):
    context = {}
    return render(request, 'design/people.html', context)

def contact(request):
    context = {}
    return render(request, 'design/contact.html', context)