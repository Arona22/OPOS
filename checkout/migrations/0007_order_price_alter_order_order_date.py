# Generated by Django 4.2 on 2023-05-11 13:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_alter_order_order_date_customer_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=datetime.datetime(2023, 5, 11, 13, 47, 9, 503907, tzinfo=datetime.timezone.utc)),
        ),
    ]
