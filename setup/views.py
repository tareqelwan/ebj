from django.shortcuts import render
from .models import Salesman

# Create your views here.

def salesman_list(request):
    salesman=Salesman.objects.all()
    context={'data': salesman}
    return render(request,'setup/salesman_list.html',context)

def salesman_detail(request,id):
    salesman=Salesman.objects.get(id=id)
    context={'data': salesman}
    return render(request,'setup/salesman_detail.html',context)