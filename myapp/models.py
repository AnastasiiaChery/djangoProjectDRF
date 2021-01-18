from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=10)
    salary = models.IntegerField(default=0)

    class Meta:
        db_table='employee'