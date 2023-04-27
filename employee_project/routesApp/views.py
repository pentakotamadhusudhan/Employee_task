from rest_framework import viewsets
from .serilaizers import SnippetSerializer, projectserializer
from django.contrib.auth.models import User
from .models import *

class popllview(viewsets.ModelViewSet):
    serializer_class = SnippetSerializer
    queryset = employeeModel.objects.all()
    lookup_field = "regId"
class projectview(viewsets.ModelViewSet):
    serializer_class = projectserializer
    queryset = projectModel.objects.all()
    lookup_field = "regId"
