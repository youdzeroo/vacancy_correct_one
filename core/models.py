from django.db import models
from companies.models import Companies


class Types(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Vacancies(models.Model):
    duration = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    terms = models.TextField()
    description = models.TextField(blank=True, null=True)
    salary = models.PositiveIntegerField(null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    type = models.ForeignKey(Types, on_delete=models.CASCADE)
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)

    def __str__(self):
        return self.position

