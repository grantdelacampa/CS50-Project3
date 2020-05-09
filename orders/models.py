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
class dinner_plate(models.Model):
    SMALL = 'sm'
    LARGE = 'lr'
    GARDEN = 'gas'
    GREEK = 'grs'
    ANTIPASTO = 'apo'
    ZITI = 'bkz'
    MEATBALL = 'mbp'
    CHICKEN = 'ckp'
    SIZE = [
        (SMALL, 'Small'),
        (LARGE, 'Large')
    ]
    TYPE = [
        (GARDEN, 'Garden Salad'),
        (GREEK, 'Greek Salad'),
        (ANTIPASTO, 'Antipasto'),
        (ZITI, 'Baked Ziti'),
        (MEATBALL, 'Meatball Parm'),
        (CHICKEN, 'Chicken Parm')
    ]
    size = models.CharField(max_length = 2, choices = SIZE, default=SMALL)
    name = models.CharField(max_length = 3, choices = TYPE, default=GARDEN)

    def price(self):
        prices = {
            'sm':{
                'gas': '40.00',
                'grs': '50.00',
                'apo': '50.00',
                'bkz': '40.00',
                'mbp': '50.00',
                'ckp': '55.00'
            },
            'lr':{
                'gas': '65.00',
                'grs': '75.00',
                'apo': '75.00',
                'bkz': '65.00',
                'mbp': '75.00',
                'ckp': '85.00'
            }
        }
        return prices[self.size][self.name]
    
    def __str__(self):
        return f"{self.size} {self.name}"

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
                    'ch': 12.70,
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

    def price(self):
        prices = {
            'sm': {
                'chs': '6.50',
                'itl': '6.50',
                'hmc': '6.50',
                'mtb': '6.50',
                'tun': '6.50',
                'tky': '7.50',
                'cpg': '7.50',
                'epg': '6.50',
                'stk': '6.50',
                'skc': '6.95',
                'spo': '8.50',
                'hbg': '4.60',
                'cbg': '5.10',
                'fck': '6.95',
                'vge': '6.95'
            },
            'lr': {
                'chs': '7.95',
                'itl': '7.95',
                'hmc': '7.95',
                'mtb': '7.95',
                'tun': '7.95',
                'tky': '8.50',
                'cpg': '8.50',
                'epg': '7.95',
                'stk': '7.95',
                'skc': '8.50',
                'spo': '8.50',
                'hbg': '6.95',
                'cbg': '7.45',
                'fck': '8.50',
                'vge': '8.50'
            }
        }
        return prices[self.size][self.name]
    
    def can_addon(self):
        if self.name == 'skc':
            return True;
        else:
            return False;
    
    def __str__(self):
        if self.addons == None:
            return f"{self.size} {self.name}"
        else:
            return f"{self.size} {self.name} with {self.addons}"
        
class pasta(models.Model):
    MOZZARELLA = 'bzmo'
    MEATBALLS = 'bzme'
    CHICKEN = 'bzch'
    TYPE = [
        (MOZZARELLA, 'Baked Ziti w/Mozzarella'),
        (MEATBALLS, 'Baked Ziti w/Meatballs'),
        (CHICKEN, 'Baked Ziti w/Chicken')
    ]
    name = models.CharField(max_length = 4, choices = TYPE, default = MOZZARELLA)

    def price(self):
        prices = {
            'bzmo':'6.50',
            'bzme':'8.75',
            'bzch':'9.75'
        }
        return prices[self.name]
    
    def __str__(self):
        return f"{self.name}"

class salad(models.Model):
    GARDEN = 'gas'
    GREEK = 'grs'
    ANTIPASTO = 'apo'
    SALAD_TUNA = 'swt'
    TYPE = [
        (GARDEN, 'Garden Salad'),
        (GREEK, 'Greek Salad'),
        (ANTIPASTO, 'Antipasto'),
        (SALAD_TUNA, 'Salad w/Tuna')
    ]
    name = models.CharField(max_length = 3, choices = TYPE, default = GARDEN)

    def price(self):
        prices = {
            'gas': '6.25',
            'grs': '8.25',
            'apo': '8.25',
            'swt': '8.25'
        }
        return prices[self.name]
    
    def __str__(self):
        return f"{self.name}"
