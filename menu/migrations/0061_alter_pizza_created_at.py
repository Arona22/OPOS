# Generated by Django 4.2.1 on 2023-05-12 15:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0060_alter_pizza_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 5, 12, 15, 47, 30, 142776, tzinfo=datetime.timezone.utc)),
        ),
    ]
