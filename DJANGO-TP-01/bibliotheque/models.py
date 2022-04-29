from django.db import models


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
    date_de_commande = models.DateField(null=True, blank=True)
    marque = models.ForeignKey(Marque, on_delete=models.SET_NULL, null=True)
    modele = models.ForeignKey(Modele, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name 

    def dico(self):
        return {"marque" : self.marque, "modele" : self.modele, "date_de_commande" : self.date_de_commande}
        
