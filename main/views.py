from django.shortcuts import render
from .models import Price, Plan, Recording


def index(request):
    return render(request, 'index.html')

def register(request):
    price = Price.objects.all()
    plans = Plan.objects.all()
    record = Recording.objects.all()
    return render(request, 'edit.html', {'price': price, 'plans': plans, 'record': record})