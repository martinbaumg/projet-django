from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import LivreForm
from . import  models
from django import forms
from bibliotheque.models import Mouvement
# from .forms import MouvementForm

def ajout(request):
    mouvement = Mouvement.objects.all()
    if request.method == "POST":
        form = LivreForm(request)
        if form.is_valid():
            livre = form.save()
            mouvement = mouvement.save()
            return HttpResponseRedirect("/")
        else:
            return render(request,"ajout.html",{"form": form, "mouvement": mouvement})
    else :
        form = LivreForm()
        return render(request,"ajout.html",{"form" : form, "mouvement": mouvement})

# def ajout(request):
#     mouvement = Mouvement.objects.all()
#     return render(request, 'ajout.html', context={"mouvement": mouvement})


def show(request):
    showmouv=Mouvement.objects.all()
    return render(request, 'show.html', {"Mouvement": showmouv})


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
    mouvement = Mouvement.objects.all()
    liste = list(models.Livre.objects.all())
    return render(request, 'livre.html', {'liste': liste, 'mouvement': mouvement})


# def test(request):
#     if request.method=="POST":
#         if request.POST.get('mouvement_litteraire'):
#             savevalue=Mouvement()
#             savevalue.mouvement_litteraire=request.POST.get('mouvement_litteraire')
#             savevalue.save()
#             messages.success(request,'Votre mouvement' +savevalue.mouvement_litteraire+ 'a été enregistré')
#             return render(request, 'menu.html')
#     else:
#             return render(request, 'menu.html')


