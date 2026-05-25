from django.shortcuts import render
from .models import *

def index(request):
    return render(request, 'index.html')

def rules(request):
    return render(request, 'rules.html')

def client(request):
    updates_data = Updates.objects.order_by('-id')[:3]

    return render(request, 'client.html', {'updates_data': updates_data})

def faq(request):
    return render(request, 'faq.html')

def games(request):
    return render(request, 'games.html')

def management(request):
    return render(request, 'management.html')

def page_not_found(request, exception):
    return render(request, '404.html', status=404)