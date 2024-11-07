from django.http import HttpResponse
from django.template import loader
from .models import Produit

def produit_list(request):
    template = loader.get_template('Produit.html')
    produits = Produit.objects.all().values()  # Query all Produit objects
    context = {
        'produits': produits,
    }
    return HttpResponse(template.render(context, request))