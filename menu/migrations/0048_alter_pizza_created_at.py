# Generated by Django 4.2.1 on 2023-05-12 14:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0047_alter_pizza_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 5, 12, 14, 52, 50, 421257, tzinfo=datetime.timezone.utc)),
        ),
    ]
