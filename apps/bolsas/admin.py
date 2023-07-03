from django.contrib import admin
from apps.bolsas.models import Hemocentro
from apps.bolsas.models import BloodBag

class ListHemocentros(admin.ModelAdmin):
    list_display = ("id", "address", "last_updated", "ideal_qnt")
    list_display_links = ("id", "address")
    search_fields = ("address",)
    list_per_page = 10

admin.site.register(Hemocentro, ListHemocentros)

class ListBags(admin.ModelAdmin):
    list_display = ("id", "type", "level", "ideal_qnt", "total", "last_updated", "location")
    list_display_links = ("id", "type")
    search_fields = ("type",)
    list_filter = ('type',)
    list_per_page = 10

admin.site.register(BloodBag, ListBags)
