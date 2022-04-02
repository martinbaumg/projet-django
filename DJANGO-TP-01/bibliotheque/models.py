from django.db import models



class Livre(models.Model): 
    titre = models.CharField(max_length=100) 
    auteur = models.CharField(max_length = 100)
    date_parution = models.DateField(blank=True, null = True) 
    nombre_pages = models.IntegerField(blank=False) 
    resume = models.TextField(null = True, blank = True) 

    def __str__(self):
        chaine = f"{self.titre} écrit par {self.auteur} avec {self.nombre_pages} pages"
        return chaine

    def dico(self):
        return {"titre" : self.titre, "auteur" : self.auteur, "date_parution" : self.date_parution, "nombre_pages" : self.nombre_pages, "resume" : self.resume }

class Mouvement(models.Model):
    mouvement_litteraire = models.CharField(max_length=100)