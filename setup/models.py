from django.db import models

class Salesman(models.Model):
    name=models.CharField(max_length=50)
    aname=models.CharField(max_length=50)
    commision=models.DecimalField(max_digits=12,decimal_places=2, default=0)
    discontinue=models.IntegerField(default=0)

    def __str__(self):
        return (self.name)
