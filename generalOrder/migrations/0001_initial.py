# Generated by Django 3.0.5 on 2020-12-30 21:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralOrder',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('student_name', models.CharField(default='null', max_length=50)),
                ('item_name', models.CharField(default='null', max_length=50)),
                ('quantity', models.IntegerField(default=-1)),
                ('price', models.IntegerField(default=-1)),
                ('additional_comments', models.CharField(default='null', max_length=300)),
                ('isOrdered', models.BooleanField(default=False)),
                ('status', models.TextField(blank=True)),
                ('order_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('current_quantity', models.IntegerField()),
            ],
        ),
    ]
