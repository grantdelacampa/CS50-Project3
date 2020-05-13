# Generated by Django 3.0.6 on 2020-05-12 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_auto_20200512_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='toppings',
            field=models.ManyToManyField(to='orders.Topping'),
        ),
        migrations.AlterField(
            model_name='pizzaorder',
            name='pizza_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='orders.Pizza'),
        ),
    ]
