# Generated by Django 4.2 on 2023-05-03 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0014_alter_categories_pizza'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='pizza',
        ),
        migrations.AddField(
            model_name='pizzas',
            name='categories',
            field=models.ManyToManyField(related_name='pizzas', to='menu.categories'),
        ),
    ]
