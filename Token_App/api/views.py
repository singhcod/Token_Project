
from django.shortcuts import render,redirect

from  Token_App.models import Employee
from Token_App.api.serializers import EmployeeSerializer
from rest_framework import viewsets

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser

class Employee_ModelViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminUser,)








