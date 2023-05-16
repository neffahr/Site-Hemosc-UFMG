from django.urls import path
from apps.bolsas.views import \
    index

urlpatterns = [
    path('', index, name='index'),
]