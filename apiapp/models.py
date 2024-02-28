from django.db import models

# Create your models here.
class Student(models.Model):
    stud_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    department = models.CharField(max_length=30)
    mark = models.FloatField()
    isplaced = models.BooleanField(default=False)