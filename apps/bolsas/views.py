from django.shortcuts import get_object_or_404, render, redirect
from apps.bolsas.models import Hemocentro, BloodBag, IndexBag
from apps.bolsas.forms import HemocentroForms
index_bags = [IndexBag("A+"), IndexBag("B+"), IndexBag("AB+"), IndexBag("O+"), 
              IndexBag("A-"), IndexBag("B-"), IndexBag("AB-"), IndexBag("O-")]

def index(request):
    lc = Hemocentro.objects.all()
    return render(request, 'bolsas/index.html', {'locations': lc, 'bags': index_bags})

def locations(request):
    lc = Hemocentro.objects.all()
    return render(request, 'bolsas/locations.html', {'locations': lc})

def historico(request):
    return render(request, 'bolsas/historico.html')

def location_info(request, location):
    lc_all = Hemocentro.objects.all()
    hc = Hemocentro.objects.filter(address=location)
    return render(request, 'bolsas/hemocentro.html', {'hc': hc, 'locations': lc_all})
