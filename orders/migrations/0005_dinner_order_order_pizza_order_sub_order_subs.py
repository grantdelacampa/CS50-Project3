# Generated by Django 3.0.6 on 2020-05-08 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20200508_1542'),
    ]

    operations = [
        migrations.CreateModel(
            name='dinner_order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='pizza_order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='sub_order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='subs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('sm', 'Small'), ('lr', 'Large')], default='sm', max_length=2)),
                ('name', models.CharField(choices=[('chs', 'Cheese'), ('itl', 'Italian'), ('hmc', 'Ham & Cheese'), ('mtb', 'Meatball'), ('tun', 'Tuna'), ('tky', 'Turkey'), ('cpg', 'Chicken Parmagiana'), ('epg', 'Eggplant Parmagiana'), ('stk', 'Steak'), ('skc', 'Steak and Cheese'), ('spo', 'Sausage, Peppers & Onions'), ('hbg', 'Hamburger'), ('cbg', 'Cheeseburger'), ('fck', 'Fried Chicken'), ('vge', 'Veggie')], default='chs', max_length=3)),
                ('addons', models.CharField(default=None, max_length=15)),
            ],
        ),
    ]