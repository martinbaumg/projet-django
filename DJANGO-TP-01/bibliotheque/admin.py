from django.contrib import admin
# from bibliotheque.models import Livre, Mouvement

# @admin.register(Mouvement)
# class MouvementAdmin(admin.ModelAdmin):
#     list_display = ['mouvement_litteraire']

# admin.site.register(Livre)
# admin.site.register(Mouvement)

from django.contrib import admin
from .models import Voiture, Marque, Modele


admin.site.register(Voiture)
admin.site.register(Marque)
admin.site.register(Modele)