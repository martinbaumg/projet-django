from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class LivreForm(ModelForm):
    class Meta:
        model = models.Livre
        fields = ('titre', 'auteur', 'date_parution', 'nombre_pages','resume', 'mouvement')
        labels = {
            'titre' : _('Titre'),
            'auteur' : _('Auteur') ,
            'date_parution' : _('date de parution'),
            'nombre_pages' : _('nombres de pages'),
            'resume' : _('Résumé'),
            'mouvement' : _('Mouvement Littéraire')
        }
        localized_fields = ('date_parution',)

# class MouvementForm(ModelForm):
#     class Meta:
#         model = models.Mouvement
#         fields = ('mouvement_litteraire',)
#         labels = {
#             'mouvement_litteraire' : _('Mouvement Litteraire')
#         }