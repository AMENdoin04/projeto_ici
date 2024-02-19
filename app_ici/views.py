from django.shortcuts import render
from django.http import HttpResponse
from django.db import transaction
from .models import Eventos, Versiculo, Proxs_lives, Imagem_carosel

def lista_de_eventos(request):
    eventos = Eventos.objects.all()
    versiculo = Versiculo.objects.all()
    proxs_lives = Proxs_lives.objects.all()
    imagens_carosels = Imagem_carosel.objects.all()
    for imagem in imagens_carosels:
        if imagem.lugar == "pri":
            pri = imagem.img.url
        if imagem.lugar == "seg":
            seg = imagem.img.url
        if imagem.lugar == "ter":
            ter = imagem.img.url
    return render(request, "index.html", {"eventos": eventos, "versiculos": versiculo, "proxs_lives": proxs_lives, "pri": pri, "seg": seg, "ter": ter})


def eventos_listados(request):
    eventos = Eventos.objects.all()
    return render(request, "lista.html", {"eventos": eventos})

def dizimos(request):
    return render(request, "dizimos.html")