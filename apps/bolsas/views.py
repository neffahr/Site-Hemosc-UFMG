from django.shortcuts import get_object_or_404, render, redirect
from apps.bolsas.models import Hemocentro
from apps.bolsas.forms import HemocentroForms

def index(request):
    lc = Hemocentro.objects.all()
    return render(request, 'bolsas/index.html', {'locations': lc})

def locations(request):
    return render(request, 'bolsas/locations.html')

def historico(request):
    return render(request, 'bolsas/historico.html')

def location_info(request, location):
    lc_all = Hemocentro.objects.all()
    hc = Hemocentro.objects.filter(address=location)
    return render(request, 'bolsas/hemocentro.html', {'hemocentro': hc, 'locations': lc_all})
