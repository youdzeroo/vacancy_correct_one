from django.shortcuts import render
from core.serializers import VacancySerializer, TypeSerializer
from rest_framework.viewsets import ModelViewSet
from core.models import Vacancies, Types


class VacanciesView(ModelViewSet):
    queryset = Vacancies.objects.all()
    serializer_class = VacancySerializer


class TypesView(ModelViewSet):
    queryset = Types.objects.all()
    serializer_class = TypeSerializer

