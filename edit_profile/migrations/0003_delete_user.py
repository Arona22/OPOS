# Generated by Django 4.2 on 2023-05-08 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edit_profile', '0002_alter_user_phone'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
