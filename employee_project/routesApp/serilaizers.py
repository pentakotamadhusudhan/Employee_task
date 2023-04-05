from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class SnippetSerializer(serializers.ModelSerializer):
    class Meta :
        model = User
        fields = ['id','username', "password", "email"]
