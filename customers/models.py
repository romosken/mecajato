from enum import auto
from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    document = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return {"name":self.name,"surname":self.surname,"email":self.email, "document":self.document}
    


class Car(models.Model):
    model = models.CharField(max_length=50)
    plate = models.CharField(max_length=10, unique=True)
    year = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    washes = models.IntegerField(default=0)
    fixes = models.IntegerField(default=0)
