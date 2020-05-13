from django.http import HttpResponse
from django.shortcuts import render

from orders.models import Salad, Pasta, DinnerPlatter, Sub
from orders.forms import PizzaForm

# Create your views here.
def index(request):

    form = PizzaForm()
    
    context = {
        "salads": Salad.objects.all(),
        "pastas": Pasta.objects.all(),
        "dinnerplatters": DinnerPlatter.objects.all(),
        "subs": Sub.objects.all(),
        "form": form
    }
    return render(request, "orders/index.html", context)
