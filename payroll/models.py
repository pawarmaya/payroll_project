

# Create your models here.
from django.db import models

class Employee(models.Model):
    emp_no = models.IntegerField(primary_key=True)
    basic_pay = models.DecimalField(max_digits=10, decimal_places=2)
    it_percent = models.DecimalField(max_digits=5, decimal_places=2)

class Attendance(models.Model):
    emp_no = models.ForeignKey(Employee, on_delete=models.CASCADE)
    month = models.CharField(max_length=20)
    days_present = models.IntegerField()

