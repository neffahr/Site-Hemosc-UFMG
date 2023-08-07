from django.contrib import admin
from apps.bolsas.models import Hemocentro, BloodBag, DataArray

class ListHemocentros(admin.ModelAdmin):
    list_display = ("id", "address", "last_updated",)
    list_display_links = ("id", "address")
    search_fields = ("address",)

admin.site.register(Hemocentro, ListHemocentros)

class ListBags(admin.ModelAdmin):
    list_display = ("id", "type", "level", "ideal_qnt", "total", "last_updated", "location")
    list_display_links = ("id", "type")
    search_fields = ("type",)
    list_filter = ('type',)
    list_per_page = 10
admin.site.register(BloodBag, ListBags)

class ListData(admin.ModelAdmin):
    list_display = ("id", "total", "bag",)
    list_display_links = ("total",)
admin.site.register(DataArray, ListData)


