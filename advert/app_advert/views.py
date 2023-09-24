from django.shortcuts import render
from .models import Advert

def index(request):
    advert = Advert.objects.all()
    context = {'advert': advert}
    return render(request, 'index.html', context)

def top_sellers(request):
    return render(request, 'top-sellers.html')

def advertisement_post(request):
    return render(request, 'advertisement-post.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def profile(request):
    return render(request, 'profile.html')

def adv(request):
    return render(request, 'advertisement.html')
