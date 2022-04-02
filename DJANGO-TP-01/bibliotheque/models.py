from django.db import models



mouvement_litteraire = (
    ('','Nouveau Roman'),
    ('', 'Surréalisme'),
    ('','Symbolisme'),
    ('','Naturalisme'),
    ('','Réalisme'),
    ('','Romantisme'),
    ('','Lumières'),
    ('','Classicisme'),
    ('','Humanisme'),
    ('','Baroque'),
    ('','Autre'),
)

class Livre(models.Model): 
    titre = models.CharField(max_length=100) 
    auteur = models.CharField(max_length = 100)
    date_parution = models.DateField(blank=True, null = True) 
    nombre_pages = models.IntegerField(blank=False) 
    resume = models.TextField(null = True, blank = True) 
    mouvement_litteraire = models.CharField(max_length=6, choices=mouvement_litteraire, blank=True)

    def __str__(self):
        chaine = f"{self.titre} écrit par {self.auteur} avec {self.nombre_pages} pages, appartenant au genre {self.mouvement_litteraire}"
        return chaine

    def dico(self):
        return {"titre" : self.titre, "auteur" : self.auteur, "date_parution" : self.date_parution, "nombre_pages" : self.nombre_pages, "resume" : self.resume, "mouvement_litteraire" : self.mouvement_litteraire}

class Mouvement(models.Model):
    mouvement_litteraire = models.CharField(max_length=100)