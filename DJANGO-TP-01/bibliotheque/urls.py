from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index),
    path('ajout/',views.ajout),
    path("traitement/",views.traitement),
    path("affiche/<int:id>/",views.affiche),
    path("delete/<int:id>",views.delete),
    path("update/<int:id>",views.update),
    path("traitementupdate/<int:id>",views.traitementupdate),
    path("tous/", views.tous),
    path('ajax/load-modele/', views.load_modele, name='ajax_load_modele'),
    path('test', views.test),
]