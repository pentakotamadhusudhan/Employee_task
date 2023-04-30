from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from ..models import employeeModel
from ..serilizers import *


class Employee_get(generics.ListAPIView):
    serializer_class = get_serializer
    permission_classes = [IsAuthenticated]
    queryset = employeeModel.objects.all()