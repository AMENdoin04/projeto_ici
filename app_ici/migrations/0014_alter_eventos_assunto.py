# Generated by Django 4.2.5 on 2023-10-06 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_ici', '0013_remove_eventos_obs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventos',
            name='assunto',
            field=models.TextField(max_length=255),
        ),
    ]
