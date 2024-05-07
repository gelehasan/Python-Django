from django.db import models

# Create your models here.

class Hello(models.Model):
    text=models.CharField(max_length=200)


class Person(models.model):
    name=models.CharField(max_length=500, null=false, blank=False, db_index=True)
    age=models.IntegerField(null=False, blank=True)

    def __str__(self):
        return self.name

