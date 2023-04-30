from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
Gender = [
    ('MALE', 'Male'),
    ('FEMALE', 'Female'),

]


class employeeModel(models.Model):
    regId = models.CharField(primary_key=True,max_length=100)
    Name = models.CharField(max_length=200)
    Email = models.EmailField(unique=True,)
    Age = models.IntegerField()
    Gender = models.CharField(max_length=100,choices=Gender)
    PhoneNo = models.CharField(max_length=14, unique=True)
    AddressDetails = models.TextField()
    HouseNo = models.CharField(max_length=200)
    Street = models.CharField(max_length=200)
    City = models.CharField(max_length=200)
    State = models.CharField(max_length=200)
    Photo = models.ImageField(upload_to="upload")
    objects = models.Manager




class projectModel(models.Model):
    regId = models.ForeignKey(employeeModel,on_delete=models.CASCADE,related_name='project')
    title = models.CharField(max_length=1000)
    description = models.TextField(max_length=1000)
    objects = models.Manager



class qualificationModel(models.Model):
    regId = models.ForeignKey(employeeModel,on_delete=models.CASCADE,related_name='qualifications')
    qualificationName = models.TextField(max_length=1000)
    fromDate = models.DateField()
    toDate = models.DateField()
    percentage =models.IntegerField()
    objects = models.Manager

    
class work_Experience(models.Model):
    regId = models.ForeignKey(employeeModel,on_delete=models.CASCADE,related_name='workexper')
    workExperience = models.CharField(max_length=1000)
    companyName = models.CharField(max_length=200)
    fromDate = models.DateField()
    toDate = models.DateField(max_length=200)
    companyAddress = models.CharField(max_length=200)
    objects = models.Manager
