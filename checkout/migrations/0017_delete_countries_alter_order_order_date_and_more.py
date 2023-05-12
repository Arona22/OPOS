# Generated by Django 4.2.1 on 2023-05-12 14:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0016_alter_contactinfo_country_alter_order_order_date_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Countries',
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=datetime.datetime(2023, 5, 12, 14, 59, 1, 301368, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='pament_date',
            field=models.DateField(default=datetime.datetime(2023, 5, 12, 14, 59, 1, 302392, tzinfo=datetime.timezone.utc)),
        ),
    ]
