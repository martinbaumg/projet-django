# Generated by Django 4.0.3 on 2022-04-03 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bibliotheque', '0004_alter_livre_mouvement_litteraire'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livre',
            name='mouvement_litteraire',
        ),
    ]
