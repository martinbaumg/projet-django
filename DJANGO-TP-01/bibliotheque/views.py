from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import LivreForm
from . import  models
from django import forms

def ajout(request):
    if request.method == "POST":
        form = LivreForm(request)
        if form.is_valid():
            livre = form.save()
            return HttpResponseRedirect("/")
        else:
            return render(request,"ajout.html",{"form": form})
    else :
        form = LivreForm()
        return render(request,"ajout.html",{"form" : form})

def traitement(request):
    lform = LivreForm(request.POST)
    if lform.is_valid():
        livre = lform.save()
        return HttpResponseRedirect("../tousleslivres")
    else:
        return render(request,"ajout.html",{"form": lform})


def index(request):
    liste = list(models.Livre.objects.all())
    return render(request, 'index.html', {'liste': liste})

def affiche(request, id):
    livre = models.Livre.objects.get(pk=id)
    return render(request,"affiche.html",{"livre" : livre})

def delete(request, id):
    livre = models.Livre.objects.get(pk=id)
    livre.delete()
    return HttpResponseRedirect("../tousleslivres")

def update(request, id):
    livre = models.Livre.objects.get(pk=id)
    lform = LivreForm(livre.dico())
    return render(request, "update.html", {"form": lform,"id":id})

def traitementupdate(request, id):
    lform = LivreForm(request.POST)
    if lform.is_valid():
        livre = lform.save(commit=False)
        livre.id = id;
        livre.save()
        return HttpResponseRedirect("../tousleslivres")
    else:
        return render(request, "update.html", {"form": lform, "id": id})

def tous(request):
    liste = list(models.Livre.objects.all())
    return render(request, 'livre.html', {'liste': liste})

def test(request):
    ctx = {}
    if request.method == 'POST':
        myForm = MyForm(request.POST)
        if myForm.is_valid():
            r = myForm.save(commit=False)
            ## ... ici je peux manipuler les éléments de mon formulaire
            r.save()
    else : myForm = MyForm()
    ctx['myForm'] = myForm
    return render(request, 'menu.html', ctx)