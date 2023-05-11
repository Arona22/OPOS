# Generated by Django 4.2.1 on 2023-05-11 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0003_offers_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfferImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(blank=True, max_length=9999)),
                ('offer', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='offers.offers')),
            ],
        ),
    ]
