
from django.db import models
from django.contrib.auth.models import User


class Student_table(models.Model):
  
    reg_no = models.IntegerField(unique=True)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    marks = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateField()

    def __str__(self):
        return self.name
