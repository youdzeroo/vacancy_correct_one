from django.shortcuts import render
from companies.serializers import CompanySerializer
from rest_framework.viewsets import ModelViewSet
from companies.models import Companies
from rest_framework import permissions, renderers,viewsets


class CompaniesView(ModelViewSet):
    queryset = Companies.objects.all()
    serializer_class = CompanySerializer
    renderer_classes = (renderers.JSONRenderer, renderers.TemplateHTMLRenderer)

    def list(self, request, *args, **kwargs):
        response = super(SnippetViewSet, self).list

