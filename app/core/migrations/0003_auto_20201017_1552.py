# Generated by Django 2.1.15 on 2020-10-17 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20201017_1532'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='gamertag',
        ),
    ]
