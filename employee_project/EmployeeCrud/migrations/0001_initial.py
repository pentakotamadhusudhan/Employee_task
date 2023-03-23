# Generated by Django 4.1.5 on 2023-03-21 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmpId', models.CharField(max_length=100)),
                ('Name', models.CharField(max_length=200)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Age', models.IntegerField()),
                ('Gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=100)),
                ('PhoneNo', models.CharField(max_length=10)),
                ('AddressDetails', models.TextField()),
                ('HouseNo', models.CharField(max_length=200)),
                ('Street', models.CharField(max_length=200)),
                ('City', models.CharField(max_length=200)),
                ('State', models.CharField(max_length=200)),
                ('CompanyName', models.CharField(max_length=200)),
                ('FromDate', models.DateField()),
                ('ToDate', models.DateField(max_length=200)),
                ('CompanyAddress', models.CharField(max_length=200)),
                ('QualificationName', models.CharField(max_length=200)),
                ('Precentage', models.CharField(max_length=200)),
                ('Title', models.CharField(max_length=200)),
                ('Description', models.CharField(max_length=200)),
                ('Photo', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='qualificationmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualificationName', models.TextField(max_length=1000)),
                ('fromDate', models.DateField()),
                ('toDate', models.DateField()),
                ('percentage', models.IntegerField()),
                ('empId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qualification', to='EmployeeCrud.employeemodel')),
            ],
        ),
        migrations.CreateModel(
            name='projectmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=1000)),
                ('description', models.TextField(max_length=1000)),
                ('empId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='EmployeeCrud.employeemodel')),
            ],
        ),
    ]
