from django.shortcuts import render

from customers.apps import CustomersConfig
from .models import Customer

def customer_list(request):
    customers=Customer.objects.all()
    context={'data': customers}
    return render(request,'customers/customer_list.html',context)

def customer_details(request,id):
    customers=Customer.objects.get(id=id)
    context={'data': customers}
    return render(request,'customers/customer_detail.html',context)