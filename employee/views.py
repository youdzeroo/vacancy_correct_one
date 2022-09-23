from django.shortcuts import render
from employee.serializers import EmployeeSerializer
from rest_framework.viewsets import ModelViewSet
from employee.models import Employee


class EmployeeView(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

