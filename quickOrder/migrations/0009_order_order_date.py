# Generated by Django 3.0.5 on 2020-05-14 00:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickOrder', '0008_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=datetime.date(2020, 5, 13)),
        ),
    ]
