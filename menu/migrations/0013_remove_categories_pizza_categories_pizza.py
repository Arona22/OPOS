# Generated by Django 4.2 on 2023-05-03 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0012_remove_pizzas_category_categories_pizza'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='pizza',
        ),
        migrations.AddField(
            model_name='categories',
            name='pizza',
            field=models.ManyToManyField(to='menu.pizzas'),
        ),
    ]
