# Generated by Django 4.2 on 2023-05-03 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0008_alter_ratings_pizza_alter_sales_pizza'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizzas',
            name='price_large',
            field=models.IntegerField(default=3999),
        ),
        migrations.AlterField(
            model_name='pizzas',
            name='price_medium',
            field=models.IntegerField(default=2999),
        ),
        migrations.AlterField(
            model_name='pizzas',
            name='price_small',
            field=models.IntegerField(default=1999),
        ),
    ]
