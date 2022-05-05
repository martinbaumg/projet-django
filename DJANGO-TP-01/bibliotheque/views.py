from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import VoitureForm
from .forms import AjoutForm
from .forms import AjoutMoForm
from . import  models
from django import forms
from bibliotheque.models import Voiture
from django.urls import reverse_lazy
from .models import Voiture, Modele, Marque


def ajout(request):
    marque_id = request.GET.get('marque')
    modele = Modele.objects.filter(marque_id=marque_id).order_by('name')
    if request.method == "POST":
        form = VoitureForm(request)
        if form.is_valid():
            voiture = form.save()
            return HttpResponseRedirect("/")
        else:
            return render(request,"ajout.html",{"form": form, 'modele': modele})
    else :
        form = VoitureForm()
        return render(request,"ajout.html",{"form" : form, 'modele': modele})


def traitement(request):
    lform = VoitureForm(request.POST)
    if lform.is_valid():
        voiture = lform.save()
        return HttpResponseRedirect("../tous")
    else:
        return render(request,"ajout.html",{"form": lform})


def index(request):
    liste = list(models.Voiture.objects.all())
    return render(request, 'index.html', {'liste': liste})


def affiche(request, id):
    voiture = models.Voiture.objects.get(pk=id)
    return render(request,"affiche.html",{"voiture" : voiture})


def delete(request, id):
    voiture = models.Voiture.objects.get(pk=id)
    voiture.delete()
    return HttpResponseRedirect("../tous")


def update(request, id):
    marque_id = request.GET.get('marque')
    modele = Modele.objects.filter(marque_id=marque_id).order_by('name')
    voiture = models.Voiture.objects.get(pk=id)
    lform = VoitureForm(voiture.dico())
    return render(request, "update.html", {"form": lform,"id":id,'modele': modele})


def traitementupdate(request, id):
    lform = VoitureForm(request.POST)
    if lform.is_valid():
        voiture = lform.save(commit=False)
        voiture.id = id;
        voiture.save()
        return HttpResponseRedirect("../tous")
    else:
        return render(request, "update.html", {"form": lform, "id": id})


def tous(request):
    voiture = list(models.Voiture.objects.all())
    marque = list(models.Marque.objects.all())
    modele = list(models.Modele.objects.all())
    return render(request, 'tous.html', {'voiture': voiture, 'marque': marque, 'modele': modele})


def load_modele(request):
    marque_id = request.GET.get('marque')
    modele = Modele.objects.filter(marque_id=marque_id).order_by('name')
    return render(request, 'modele_options.html', {'modele': modele})
    
def ajoutmarque(request):
    submitted = False
    if request.method == "POST":
        form = AjoutForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/ajout")
    else: 
        form = AjoutForm
        if 'submitted' in request.GET:
            submitted = True
    
    return render(request, 'ajoutmarque.html', {'form': form})
    
def ajoutmodele(request):
    submitted = False
    if request.method == "POST":
        form = AjoutMoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/ajout")
    else: 
        form = AjoutMoForm
        if 'submitted' in request.GET:
            submitted = True
    
    return render(request, 'ajoutmodele.html', {'form': form})
    

def allmarque(request):
    voiture = list(models.Voiture.objects.all())
    marque = models.Marque.objects.all()
    modele = models.Modele.objects.all()
    return render(request, 'allmarque.html', {'marque': marque, 'modele': modele, 'voiture': voiture})

def deletemarque(request, marque_id):
    marque = models.Marque.objects.get(pk=marque_id)
    marque.delete()
    return HttpResponseRedirect("../allmarque")
