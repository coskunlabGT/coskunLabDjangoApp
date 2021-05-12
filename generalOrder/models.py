from django.db import models
from django.utils import timezone


# Create your models here.

class GenOrderTable(models.Model):
    order_id = models.AutoField(primary_key = True, unique = True)
    student_name = models.CharField(max_length = 50)
    item_name = models.CharField(max_length = 50)
    quantity = models.IntegerField()
    price = models.IntegerField()
    additional_comments = models.CharField(max_length = 300)
    isOrdered = models.BooleanField(default = False)
    status = models.TextField(default = "Pending Approval")
    order_date = models.DateTimeField(default = timezone.now)

class Inventory(models.Model):
    item_name = models.CharField(max_length = 50)
    current_quantity = models.IntegerField()


