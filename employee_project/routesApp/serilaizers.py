from django.db.models import Max
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from .models import *

class SnippetSerializer(serializers.ModelSerializer):
    class Meta :
        model = employeeModel
        fields = ["Name","Email","Age","Gender","PhoneNo","AddressDetails","HouseNo","Street","City","State","Photo"]

    # def create(self, validated_data):
    #     # max_id = employeeModel.objects.all().aggregate(Max('id'))
    #     # print(max_id)
    #     # regid = validated_data['regId']
    #     re = "regid"+"madhu"
    #     user = employeeModel.objects.create(regId=re,Email = validated_data["Email"])
    #     user.save()
    #     return  user

class projectserializer(serializers.ModelSerializer):
    class Meta :
        model = projectModel
        fields = "__all__"
