from django.contrib import admin
from bibliotheque.models import Mouvement

@admin.register(Mouvement)
class MouvementAdmin(admin.ModelAdmin):
    list_display = ['mouvement_litteraire']