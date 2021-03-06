# Generated by Django 3.0.6 on 2020-05-08 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20200508_1532'),
    ]

    operations = [
        migrations.CreateModel(
            name='toppings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('pep', 'Pepperoni'), ('sas', 'Sausage'), ('mus', 'Mushrooms'), ('oni', 'Onions'), ('ham', 'Ham'), ('cbn', 'Canadian Bacon'), ('pin', 'Pineapple'), ('ept', 'Eggplant'), ('tob', 'Tomato & Basil'), ('grp', 'Green Peppers'), ('hbr', 'Hamburger'), ('sph', 'Spinach'), ('art', 'Artichoke'), ('buc', 'Buffalo Chicken'), ('bqc', 'Barbecue Chicken'), ('anc', 'Anchovies'), ('blo', 'Black Olives'), ('frg', 'Fresh Garlic'), ('zuc', 'Zucchini')], default=None, max_length=3)),
            ],
        ),
    ]
