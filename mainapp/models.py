from django.db import models

# Create your models here.

class Product(models.Model):
    objectid = models.IntegerField(unique=True)
    product_variety = models.CharField(max_length=254)
    commodity_type = models.CharField(max_length=254)
    unit = models.CharField(max_length=254)
    volume_in_kgs = models.PositiveIntegerField()
    values_in_ksh = models.FloatField()
    date = models.DateTimeField()

    def __str__(self):
        return str(self.objectid)

    class Meta:
        db_table = "products"
        verbose_name = "Product"
        verbose_name_plural = "products"