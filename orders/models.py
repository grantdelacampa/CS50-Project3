from django.db import models

# Create your models here.
"""
    TODO:
        - Implement pizza_order
        - Implement sub_order
        - Implement dinner_order
"""

# Choices for the models are defined inside the model class
# this is per the recomendation here:
# https://docs.djangoproject.com/en/3.0/ref/models/fields/#field-choices
class order(models.Model):
    #pizza_order
    #sub_order
    #dinner_order
    #salads
    #pasta
    pass
class pizza_order(models.Model):
    #pizza
    #toppings
    #price
    pass
class sub_order(models.Model):
    #sub
    #price
    pass
class dinner_order(models.Model):
    #type
    #price
    pass

class pizza(models.Model):
    SMALL = 'sm'
    LARGE = 'lr'
    REGULAR = 're'
    SICILIAN = 'sc'
    CHEESE = 'ch'
    TOPPING_1 = '1t'
    TOPPING_2 = '2t'
    TOPPING_3 = '3t'
    SPECIAL = 'sp'
    SIZE = [
        (SMALL, 'Small'),
        (LARGE, 'Large')
    ]
    CRUST = [
        (REGULAR, 'Regular Crust'),
        (SICILIAN, 'Sicilian Crust')
    ]
    TYPE = [
        (CHEESE, 'Cheese'),
        (TOPPING_1, '1 Topping'),
        (TOPPING_2, '2 Topping'),
        (TOPPING_3, '3 Topping'),
        (SPECIAL, 'Special')
    ]
    
    size = models.CharField(max_length = 2, choices = SIZE, default = SMALL)
    crust = models.CharField(max_length = 2, choices = CRUST, default = REGULAR)
    topping_type = models.CharField(max_length = 2, choices = TYPE, default = CHEESE)

    def price(self):
        prices = {
            're' : {
                'sm' : {
                    'ch': '12.70',
                    '1t': '13.70',
                    '2t': '15.20',
                    '3t': '16.20',
                    'sp': '17.75'
                },
                'lr' : {
                    'ch': '17.95',
                    '1t': '19.95',
                    '2t': '21.95',
                    '3t': '23.95',
                    'sp': '25.95'
                }
            },
            'sc': {
                'sm' : {
                    'ch': '24.45',
                    '1t': '26.45',
                    '2t': '28.45',
                    '3t': '29.45',
                    'sp': '30.45'
                },
                'lr' : {
                    'ch': '38.70',
                    '1t': '40.70',
                    '2t': '42.70',
                    '3t': '44.70',
                    'sp': '45.70'
                }
            }
        }
        cost = prices[self.crust][self.size][self.topping_type]
        return cost
            

    def __str__(self):
        return f"{self.size} {self.crust} {self.topping_type} pizza"

class topping(models.Model):
    PEPPERONI = 'pep'
    SAUSAGE = 'sas'
    MUSHROOMS = 'mus'
    ONIONS = 'oni'
    HAM = 'ham'
    CANADIAN_BACON = 'cbn'
    PINEAPPLE = 'pin'
    EGGPLANT = 'ept'
    TOMATO_BASIL = 'tob'
    GREEN_PEPPERS = 'grp'
    HAMBURGER = 'hbr'
    SPINACH = 'sph'
    ARTICHOKE = 'art'
    BUFFALO_CHICKEN = 'buc'
    BARBECUE_CHICKEN = 'bqc'
    ANCHOVIES = 'anc'
    BLACK_OLIVES = 'blo'
    FRESH_GARLIC = 'frg'
    ZUCCHINI = 'zuc'
    TOPPINGS = [
        (PEPPERONI, 'Pepperoni'),
        (SAUSAGE, 'Sausage'),
        (MUSHROOMS, 'Mushrooms'),
        (ONIONS, 'Onions'),
        (HAM, 'Ham'),
        (CANADIAN_BACON, 'Canadian Bacon'),
        (PINEAPPLE, 'Pineapple'),
        (EGGPLANT, 'Eggplant'),
        (TOMATO_BASIL, 'Tomato & Basil'),
        (GREEN_PEPPERS, 'Green Peppers'),
        (HAMBURGER, 'Hamburger'),
        (SPINACH, 'Spinach'),
        (ARTICHOKE, 'Artichoke'),
        (BUFFALO_CHICKEN, 'Buffalo Chicken'),
        (BARBECUE_CHICKEN, 'Barbecue Chicken'),
        (ANCHOVIES, 'Anchovies'),
        (BLACK_OLIVES, 'Black Olives'),
        (FRESH_GARLIC, 'Fresh Garlic'),
        (ZUCCHINI, 'Zucchini')
    ]
    name = models.CharField(max_length = 3, choices = TOPPINGS)

    def __str__(self):
        return f"{self.name}"

class subs(models.Model):
    SMALL = 'sm'
    LARGE = 'lr'
    CHEESE = 'chs'
    ITALIAN = 'itl'
    HAM_CHEESE = 'hmc'
    MEATBALL = 'mtb'
    TUNA = 'tun'
    TURKEY = 'tky'
    CHICKEN_PARMAGIANA = 'cpg'
    EGGPLANT_PARMAGIANA = 'epg'
    STEAK = 'stk'
    STEAK_CHEESE = 'skc'
    SASAUGE_PEPPERS_ONIONS = 'spo'
    HAMBURGER = 'hbg'
    CHEESEBURGER = 'cbg'
    FRIED_CHICKEN = 'fck'
    VEGGIE = 'vge'
    
    SIZE = [
        (SMALL, 'Small'),
        (LARGE, 'Large')
    ]
    TYPE = [
        (CHEESE, "Cheese"),
        (ITALIAN, "Italian"),
        (HAM_CHEESE, "Ham & Cheese"),
        (MEATBALL, "Meatball"),
        (TUNA, "Tuna"),
        (TURKEY, "Turkey"),
        (CHICKEN_PARMAGIANA, "Chicken Parmagiana"),
        (EGGPLANT_PARMAGIANA, "Eggplant Parmagiana"),
        (STEAK, "Steak"),
        (STEAK_CHEESE, "Steak and Cheese"),
        (SASAUGE_PEPPERS_ONIONS, "Sausage, Peppers & Onions"),
        (HAMBURGER, "Hamburger"),
        (CHEESEBURGER, "Cheeseburger"),
        (FRIED_CHICKEN, "Fried Chicken"),
        (VEGGIE, "Veggie")
    ]
    size = models.CharField(max_length = 2, choices = SIZE, default = SMALL)
    name = models.CharField(max_length = 3, choices = TYPE, default = CHEESE)
    addons = models.CharField(max_length = 15, default = None)
    
    def additional_addons(self):
        if self.name == 'skc':
            return True;
        else:
            return False;
        
    def __str__(self):
        if self.addons == None:
            return f"{self.size} {self.name}"
        else:
            return f"{self.size} {self.name} with {self.addons}"
