# Generated by Django 4.2 on 2023-05-04 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0019_ratings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ratings',
            name='id',
        ),
        migrations.RemoveField(
            model_name='ratings',
            name='pizza',
        ),
        migrations.AddField(
            model_name='ratings',
            name='name',
            field=models.CharField(blank=True, max_length=255, primary_key=True, serialize=False),
        ),
    ]
