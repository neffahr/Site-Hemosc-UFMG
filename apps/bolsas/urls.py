from django.urls import path
from apps.bolsas.views import \
    index, locations, historico, location_info, search

urlpatterns = [
    path('', index, name='index'),
    path('locations/', locations, name='locations'),
    path('historico/', historico, name='historico'),
    path('hemocentro/<str:location>', location_info, name='hemocentro'),
    path('search/', search, name='search'),
]