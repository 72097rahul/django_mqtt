from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializer import *

def get_data(data):
    emp= Emp.objects.get(id=data['id'])
    serial = EmpSerializer(emp)
    return serial.data
