from distutils import extension
from django.db import models

def image_upload(instance,filename):
    imagename,extension=filename.split(".")
    return "sman/%s.%s"%(instance.id,extension)

class Salesman(models.Model):
    name=models.CharField(max_length=50)
    aname=models.CharField(max_length=50)
    commision=models.DecimalField(max_digits=12,decimal_places=2, default=0)
    discontinue=models.IntegerField(default=0)
    image = models.ImageField(upload_to=image_upload)

    def __str__(self):
        return (self.name)
