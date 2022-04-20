from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
from django import forms
from .models import Voiture, Modele


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