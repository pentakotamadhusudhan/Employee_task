# Generated by Django 4.1.7 on 2023-04-27 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employeeModel',
            fields=[
                ('regId', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=200)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Age', models.IntegerField()),
                ('Gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=100)),
                ('PhoneNo', models.CharField(max_length=14, unique=True)),
                ('AddressDetails', models.TextField()),
                ('HouseNo', models.CharField(max_length=200)),
                ('Street', models.CharField(max_length=200)),
                ('City', models.CharField(max_length=200)),
                ('State', models.CharField(max_length=200)),
                ('Photo', models.TextField()),
            ],
            options={
                'db_table': 'employeeCollection',
            },
        ),
        migrations.CreateModel(
            name='work_Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workExperience', models.CharField(max_length=1000)),
                ('companyName', models.CharField(max_length=200)),
                ('fromDate', models.DateField()),
                ('toDate', models.DateField(max_length=200)),
                ('companyAddress', models.CharField(max_length=200)),
                ('regId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workExperience', to='routesApp.employeemodel')),
            ],
        ),
        migrations.CreateModel(
            name='qualificationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualificationName', models.TextField(max_length=1000)),
                ('fromDate', models.DateField()),
                ('toDate', models.DateField()),
                ('percentage', models.IntegerField()),
                ('regId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qualifications', to='routesApp.employeemodel')),
            ],
        ),
        migrations.CreateModel(
            name='projectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('description', models.TextField(max_length=1000)),
                ('regId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to='routesApp.employeemodel')),
            ],
        ),
    ]