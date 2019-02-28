from django.db import models

class Emp(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, unique=True)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10,decimal_places=2)

    class Meta:
        db_table = 'emp'
        
