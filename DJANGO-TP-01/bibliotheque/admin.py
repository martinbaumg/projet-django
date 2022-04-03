from django.contrib import admin
from bibliotheque.models import Livre, Mouvement

# @admin.register(Mouvement)
# class MouvementAdmin(admin.ModelAdmin):
#     list_display = ['mouvement_litteraire']

admin.site.register(Livre)
admin.site.register(Mouvement)