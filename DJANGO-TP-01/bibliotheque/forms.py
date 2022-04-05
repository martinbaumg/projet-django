from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
from django import forms
from .models import Voiture, Modele

# class VoitureForm(ModelForm):
#     class Meta:
#         model = models.Voiture
#         fields = ('marque', 'modele', 'date_production', 'nombre_places','puissance')
#         labels = {
#             'marque' : _('Marque'),
#             'modele' : _('Modèle') ,
#             'date_production' : _('date de production'),
#             'nombre_places' : _('nombre de places'),
#             'puissance' : _('puissance')
#         }
#         localized_fields = ('date_production',)

class VoitureForm(forms.ModelForm):
    class Meta:
        model = Voiture
        fields = ('name', 'date_production', 'marque','modele')

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