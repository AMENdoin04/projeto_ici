# Generated by Django 4.2.5 on 2023-09-27 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_ici', '0002_delete_eventos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('local', models.CharField(max_length=255)),
                ('data', models.CharField(max_length=255)),
            ],
        ),
    ]
