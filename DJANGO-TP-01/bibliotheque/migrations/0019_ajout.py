# Generated by Django 4.0.4 on 2022-04-29 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliotheque', '0018_rename_date_production_voiture_date_de_commande'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ajout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marque', models.CharField(max_length=100)),
            ],
        ),
    ]