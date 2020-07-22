from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html',{})

def clients(request):
    return render(request, 'clients/home.html',{} )

def support(request):
    return render(request, 'support/home.html', {})

def director(request):
    return render(request, 'director/home.html')