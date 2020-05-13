from django.contrib import admin
from .models import Pasta, Topping, Salad, DinnerPlatter, SubExtra, Sub, Pizza, PizzaOrder
# Register your models here.

admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(DinnerPlatter)
admin.site.register(SubExtra)
admin.site.register(Sub)
admin.site.register(Pizza)
admin.site.register(PizzaOrder)
admin.site.register(Topping)