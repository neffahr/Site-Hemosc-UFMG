from django.shortcuts import render

def index(request):
    return render(request, 'bolsas/index.html')

def locations(request):
    return render(request, 'bolsas/locations.html')

def historico(request):
    return render(request, 'historico.html')

def login(request):
    return render(request, 'login.html')
