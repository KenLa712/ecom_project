from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Produkt)
admin.site.register(Kunde)
admin.site.register(Bestellung)
# Manu Test Flux

#https://www.youtube.com/watch?v=eyP9Y5YaNw4&t=301s

class WarenkorbItemsAdmin(admin.ModelAdmin):
    list_display = ('warenkorb', 'produkt', 'anzahl')
admin.site.register(WarenkorbProdukt, WarenkorbItemsAdmin)

class WarenkorbAdmin(admin.ModelAdmin):
    list_display = ('id', 'zwischensumme', 'kunde')
admin.site.register(Warenkorb, WarenkorbAdmin)