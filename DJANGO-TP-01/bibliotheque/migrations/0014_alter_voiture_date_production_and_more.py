# Generated by Django 4.0.3 on 2022-04-04 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliotheque', '0013_voiture_delete_livre_delete_mouvement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voiture',
            name='date_production',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='voiture',
            name='nombre_places',
            field=models.CharField(default=10, max_length=100),
            preserve_default=False,
        ),
    ]
