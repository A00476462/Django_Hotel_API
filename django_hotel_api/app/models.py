from django.db import models

# Create your models here.

class Hotels(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=False, default=0.0)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)