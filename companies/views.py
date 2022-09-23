from django.shortcuts import render
from companies.serializers import CompanySerializer
from rest_framework.viewsets import ModelViewSet
from companies.models import Companies


class CompaniesView(ModelViewSet):
    queryset = Companies.objects.all()
    serializer_class = CompanySerializer
