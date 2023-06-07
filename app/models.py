from django.db import models

# Create your models here.

class Employee(models.Model):
    Ename=models.CharField(max_length=100)
    Eid=models.IntegerField(primary_key=True)
    Eage=models.IntegerField()

    def __str__(self) -> str:
        return self.Ename