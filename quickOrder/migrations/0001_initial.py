# Generated by Django 3.0.5 on 2020-06-22 18:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('UserManagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('current_quantity', models.IntegerField()),
                ('min_quantity', models.IntegerField()),
                ('refill_needed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('status', models.TextField(default='Pending Approval')),
                ('requested_quantity', models.IntegerField(default=0)),
                ('order_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('order_name', models.TextField(default='Loading...')),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QuickOrder.InventoryItem')),
                ('user', models.ForeignKey(on_delete=models.SET(0), to='UserManagement.User')),
            ],
        ),
    ]
