# Generated by Django 4.2.5 on 2023-10-09 01:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_ici', '0018_imagem_carosel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagem_carosel',
            old_name='secuencia_da_img',
            new_name='lugar',
        ),
    ]
