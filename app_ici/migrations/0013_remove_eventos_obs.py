# Generated by Django 4.2.5 on 2023-10-06 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_ici', '0012_eventos_assunto_eventos_obs_eventos_pregador_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventos',
            name='obs',
        ),
    ]
