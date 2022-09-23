from rest_framework import serializers
from core.models import Vacancies, Types


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancies
        fields = '__all__'


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Types
        fields = '__all__'