# Generated by Django 4.2 on 2023-05-04 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0017_rename_pizza_image_pizzaimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='sales',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='Ratings',
        ),
    ]
