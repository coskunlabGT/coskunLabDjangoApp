# Generated by Django 3.0.5 on 2020-05-12 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserManagement', '0001_initial'),
        ('quickOrder', '0003_inventoryitem_requested_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventoryitem',
            name='requested_quantity',
        ),
        migrations.RemoveField(
            model_name='inventoryitem',
            name='status',
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('status', models.TextField(default='Pending Approval')),
                ('requested_quantity', models.IntegerField(default=0)),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quickOrder.InventoryItem')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserManagement.User')),
            ],
        ),
    ]
