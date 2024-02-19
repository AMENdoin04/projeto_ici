from django.db import models

class Eventos(models.Model):
    nome = models.CharField(max_length=255)
    local = models.CharField(max_length=255)
    data = models.DateTimeField()
    pregador = models.CharField(null=True, max_length=255)
    assunto = models.TextField(max_length=255)
    img = models.FileField(null=True, blank=True)

    def __str__(self) -> str:
        return self.nome

class Versiculo(models.Model):
    versiculo = models.TextField(max_length=255)

    def __str__(self) -> str:
        return self.versiculo

class Proxs_lives(models.Model):
    proxs_lives = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.proxs_lives

class Imagem_carosel(models.Model):
    lugar = models.TextField(max_length=255)
    img = models.FileField(null=True, blank=True)

    def __str__(self) -> str:
        return self.lugar