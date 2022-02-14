
from django.db import models

class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=30)
    salary = models.DecimalField(max_digits=10,decimal_places=2)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.ename
