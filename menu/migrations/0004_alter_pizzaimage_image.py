# Generated by Django 4.2 on 2023-05-03 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_prices_pizza_ratings_pizza_sales_pizza_pizzaimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizzaimage',
            name='image',
            field=models.CharField(blank=True, max_length=9999),
        ),
    ]
