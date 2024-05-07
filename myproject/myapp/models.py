from django.db import models

# Create your models here.

class Hello(models.Model):
    text=models.CharField(max_length=200)


class Person(models.model):
    name=models.CharField(max_length=500, null=false, blank=False, db_index=True)
    age=models.IntegerField(null=False, blank=True)

    def __str__(self):
        return self.name

class Address(models.model):
    number=models.IntegerField( null=false, blank=True)
    street_name=models.CharField(max_length=500, null=false, blank=True)
    resident= models.ForeignKey(Person, null=True, on_delete=models.SET_NULL)


