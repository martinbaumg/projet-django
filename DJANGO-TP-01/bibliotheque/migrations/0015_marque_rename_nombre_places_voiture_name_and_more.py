# Generated by Django 4.0.3 on 2022-04-05 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bibliotheque', '0014_alter_voiture_date_production_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.RenameField(
            model_name='voiture',
            old_name='nombre_places',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='voiture',
            name='puissance',
        ),
        migrations.AlterField(
            model_name='voiture',
            name='date_production',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Modele',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('marque', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bibliotheque.marque')),
            ],
        ),
        migrations.AlterField(
            model_name='voiture',
            name='marque',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bibliotheque.marque'),
        ),
        migrations.AlterField(
            model_name='voiture',
            name='modele',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bibliotheque.modele'),
        ),
    ]
