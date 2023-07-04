from django.shortcuts import get_object_or_404, render, redirect
from apps.bolsas.models import Hemocentro, BloodBag
from apps.bolsas.forms import HemocentroForms

def calc_ideal_qnt(req_type):
    qnt = 0
    for bag in BloodBag.objects.filter(type=req_type):
        qnt += bag.ideal_qnt
    return qnt/7
def calc_total(req_type):
    qnt = 0
    for bag in BloodBag.objects.filter(type=req_type):
        qnt += bag.total
    return qnt/7

def calc_level(ideal_qnt, req_type):
    total_bags = calc_total(req_type)
    if (total_bags <= (ideal_qnt//4)):
        return 'Crítico'
    elif (total_bags <= (3*ideal_qnt//5)):
        return 'Baixo'
    elif (total_bags < (ideal_qnt)):
        return 'Estável'
    else:
        return 'Adequado'

def index(request):
    lc = Hemocentro.objects.all()
    bags = BloodBag.objects.all()
    bags_info = {'A+':[], 'B+':[], 'AB+':[], 'O+':[], 'A-':[], 'B-':[], 'AB-':[], 'O-':[]}

    for type in bags_info.keys():
        ideal_qnt = calc_ideal_qnt(type)
        bags_info[type].append(ideal_qnt)
        bags_info[type].append(calc_level(ideal_qnt, type))

    return render(request, 'bolsas/index.html', {'locations': lc, 'bags': bags_info})

def locations(request):
    return render(request, 'bolsas/locations.html')

def historico(request):
    return render(request, 'bolsas/historico.html')

def location_info(request, location):
    lc_all = Hemocentro.objects.all()
    hc = lc_all.filter(address=location)
    return render(request, 'bolsas/hemocentro.html', {'hemocentro': hc, 'locations': lc_all})
