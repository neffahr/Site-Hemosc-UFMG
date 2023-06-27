from django.shortcuts import get_object_or_404, render, redirect
from apps.bolsas.models import Hemocentro
from apps.bolsas.forms import HemocentroForms

def index(request):
    return render(request, 'bolsas/index.html')

def locations(request):
    return render(request, 'bolsas/locations.html')

def historico(request):
    return render(request, 'users/historico.html')
