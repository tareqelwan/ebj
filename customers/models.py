
from django.db import models
from setup.models import Salesman

class Customer(models.Model):

    CTYPE = (
    ('1','Company'),
    ('2','Person'),
    ('3','Government'),
    ('4','Others'),
    ('5','Super dealer'),
    ('6','Contractor'),
    ('7','Owner'),
    ('8','Hyper'),
    ('9','Power retailer'),
    )

    GCODE = (
    ('1','Customer'),
    ('2','Supplier'),    
    )


    name = models.CharField(max_length=100)
    name_arb = models.CharField(max_length=100)
    
    buildno = models.CharField(max_length=10)
    street = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    city = models.CharField(max_length=10)
    country = models.CharField(max_length=10)
    postalcode = models.CharField(max_length=10)
    additionalno= models.CharField(max_length=10)

    buildno_a = models.CharField(max_length=10)
    street_a = models.CharField(max_length=50)
    district_a = models.CharField(max_length=50)
    city_a = models.CharField(max_length=10)
    country_a = models.CharField(max_length=10)
    postalcode_a = models.CharField(max_length=10)
    additionalno_a= models.CharField(max_length=10)
    
    email= models.EmailField(max_length=30)
    phone= models.CharField(max_length=30)
    
    vat_id = models.CharField(max_length=30)
    crlimit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    crdays = models.IntegerField(default=0)
    salesman = models.ForeignKey(Salesman,on_delete=models.CASCADE,default=1)

    ctype = models.CharField(max_length=1,choices=CTYPE)
    cgroup = models.CharField(max_length=1,choices=GCODE)

    def __str__(self):
        return (self.name)

