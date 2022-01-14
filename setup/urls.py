

from django.urls import path
from . import views

urlpatterns = [    
    path('salesman/', views.salesman_list),
    path('salesman/<int:id>', views.salesman_detail),
]
