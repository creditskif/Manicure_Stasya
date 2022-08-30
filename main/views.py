from django.shortcuts import render
from .models import Price


def index(request):
    return render(request, 'index.html')

def register(request):
    price = Price.objects.all()
    return render(request, 'edit.html', {'price': price})