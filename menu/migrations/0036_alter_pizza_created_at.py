# Generated by Django 4.2 on 2023-05-11 13:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0035_alter_pizza_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 5, 11, 13, 1, 53, 226839, tzinfo=datetime.timezone.utc)),
        ),
    ]
