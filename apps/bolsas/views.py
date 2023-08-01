from django.shortcuts import get_object_or_404, render, redirect
from apps.bolsas.models import Hemocentro, BloodBag, IndexBag
from apps.bolsas.forms import HemocentroForms
from django.forms import formset_factory

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

def edit_hc(request, location):
    if not request.user.is_authenticated:
        return redirect('login')
    
    hc = Hemocentro.objects.get(address=location)
    FormSet = formset_factory(HemocentroForms, extra=6, min_num=7, validate_min=True)
    formset = FormSet(prefix = 'bag')

    if request.method == 'POST':
        formset = FormSet(request.POST, prefix = 'bag')

        if formset.is_valid():
            for bag in hc.bloodbag_set.all:
                i = 0
                entry=formset["bag-"+ str(i) + "-entry"].value()
                exit=formset["bag-"+ str(i) + "-exit"].value()
                total=bag.total + (entry - exit)
                bag.total=total
                bag.ideal_qnt = bag.calc_ideal_qnt(total)
                bag.save()
                i += 1
            
            return redirect('index')

    return render(request, 'bolsas/editar.html', {'formset': formset, 'hc': hc})

def search(request):
    lc = Hemocentro.objects.all()
    bags = BloodBag.objects.order_by('last_updated')

    if "search" in request.GET:
        type = request.GET['search']
        if type:
            bags = bags.filter(type__icontains=type)

    return render(request, 'bolsas/search.html', {'bags': bags, 'locations': lc})