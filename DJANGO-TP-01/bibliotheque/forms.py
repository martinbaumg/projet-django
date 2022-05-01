from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
from django import forms
from .models import Voiture, Modele, Marque


class VoitureForm(forms.ModelForm):
    class Meta:
        model = Voiture
        fields = ('name', 'date_de_commande', 'marque','modele')
        labels = {"modele":"Modèle", "name":"Votre nom :", "date_de_commande":"Date de commande :"}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['modele'].queryset = Modele.objects.none()

        if 'marque' in self.data:
            try:
                marque_id = int(self.data.get('marque'))
                self.fields['modele'].queryset = Modele.objects.filter(marque_id=marque_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['modele'].queryset = self.instance.marque.modele_set.order_by('name')
            
            
class AjoutForm(ModelForm):
    class Meta:
        model = Marque
        fields = ('name',)
        labels = {"name":"Nom de la marque"}

class AjoutMoForm(ModelForm):
        class Meta:
            model = Modele
            fields = ('marque', 'name',)
            labels = {"name":"Nom du modèle"}