# Generated by Django 3.0.5 on 2020-05-12 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickOrder', '0004_auto_20200512_1423'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='item_id',
            new_name='item',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user_id',
        ),
    ]
