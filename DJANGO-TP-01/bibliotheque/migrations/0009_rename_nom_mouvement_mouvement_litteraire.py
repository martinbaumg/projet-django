# Generated by Django 4.0.3 on 2022-04-03 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bibliotheque', '0008_rename_mouvement_litteraire_mouvement_nom'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mouvement',
            old_name='nom',
            new_name='mouvement_litteraire',
        ),
    ]