from django.db import models

# Create your models here.

class Customers(models.Model):
    customers_id = models.IntegerField(primary_key=True)
    address = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'customers'


class Products(models.Model):
    products_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'products'

