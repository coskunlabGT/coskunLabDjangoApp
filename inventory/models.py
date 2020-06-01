from django.db import models


# Create your models here.

class Inventory(models.Model):
    item_id = models.IntegerField(default=0,unique=True,primary_key=True)
    #non-null name
    item_name = models.CharField(max_length = 200)
    current_level = models.IntegerField(default=0)
    target_level = models.IntegerField(default=0)
    price = models.FloatField(default=0.0)
    refillNeeded = models.BooleanField(default = False)
    isOrdered = models.BooleanField(default = False)
  
    
    

    def __str__(self):
        return self.item_name