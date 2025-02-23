# Generated by Django 4.2 on 2023-05-09 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.CharField(default='', max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default='', max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.CharField(default='', max_length=9999),
        ),
    ]
