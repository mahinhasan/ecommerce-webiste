# Generated by Django 3.1.5 on 2021-01-07 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='fname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='lname',
            new_name='last_name',
        ),
    ]