# Generated by Django 3.1.5 on 2021-01-09 17:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0010_order_present'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
