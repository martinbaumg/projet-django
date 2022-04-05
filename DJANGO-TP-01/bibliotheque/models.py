from django.db import models

# mouvement = (
#     ('','BMW'),
#     ('','Mercedes'),
#     ('','Audi'),
#     ('','Peugeot'),
#     ('','Renault'),
#     ('','Dodge'),
#     ('','Fiat'),
# )

# class Voiture(models.Model): 
#     marque = models.CharField(max_length=100) 
#     modele = models.CharField(max_length = 100)
#     nombre_places = models.CharField(max_length=100) 
#     date_production = models.DateField(blank=False)
#     puissance = models.CharField(max_length=40) 
#     # mouvement = models.CharField(max_length=6, choices=mouvement, blank=True)

#     def __str__(self):
#         chaine = f"{self.modèle} produit par {self.marque} qui dispose de {self.nombre_places} fabriqué en {self.date_production}"
#         return chaine

#     def dico(self):
#         return {"marque" : self.marque, "modele" : self.modele, "nombre_places" : self.nombre_places, "date_production" : self.date_production, "puissance" : self.puissance}

# class Mouvement(models.Model):
#     mouvement_litteraire = models.CharField(max_length=100, null=False, blank=False) 

#     def __str__(self):
#         return self.mouvement_litteraire


class Marque(models.Model):
    name = models.CharField(max_length=30)
 
    def __str__(self):
        return self.name

class Modele(models.Model):
    marque = models.ForeignKey(Marque, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Voiture(models.Model):
    name = models.CharField(max_length=100)
    date_production = models.DateField(null=True, blank=True)
    marque = models.ForeignKey(Marque, on_delete=models.SET_NULL, null=True)
    modele = models.ForeignKey(Modele, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name 

    def dico(self):
        return {"marque" : self.marque, "modele" : self.modele, "date_production" : self.date_production}
