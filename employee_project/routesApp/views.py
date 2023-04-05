from rest_framework import viewsets
from .serilaizers import SnippetSerializer
from django.contrib.auth.models import User

class popllview(viewsets.ModelViewSet):
    serializer_class = SnippetSerializer
    queryset = User.objects.all()
    lookup_field = "id"
