from django.urls import path
from apps.bolsas.views import \
    index, locations, historico, login

urlpatterns = [
    path('', index, name='index'),
    path('locations/', locations, name='locations'),
    path('historico/', historico, name='historico'),
    path('login/', login, name='login'),
]