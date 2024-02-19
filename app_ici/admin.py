from django.contrib import admin
from .models import Eventos, Versiculo, Proxs_lives, Imagem_carosel
from django.conf import settings
import os

admin.site.register(Versiculo)
admin.site.register(Proxs_lives)

@admin.action(description="remover imagem junto")
def remover_imagem(modeladmin, request, queryset):
    for evento in queryset:
        print(f"{settings.MEDIA_ROOT}/{evento.img}")
        os.remove(f"{settings.MEDIA_ROOT}/{evento.img}")

@admin.register(Eventos)
class EventosAdmin(admin.ModelAdmin):
    actions = [remover_imagem,]

@admin.register(Imagem_carosel)
class EventosAdmin(admin.ModelAdmin):
    actions = [remover_imagem,]