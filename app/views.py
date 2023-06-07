from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from app.models import *

from app.serializers import *
from rest_framework.response import Response
from rest_framework import status

@api_view()
def EmployyeJData(request):
    EQS=Employee.objects.all()#LOEO
    ESD=EmployeeMS(EQS,many=True)
    return Response(ESD.data)










