from django.db import models

# Create your models here.

class Produit(models.Model):
    nom= models.CharField(max_length=50)
    quantite= models.IntegerField()
    description= models.TextField()
    prix= models.FloatField()
    date_publication= models.DateField(auto_now=True)

