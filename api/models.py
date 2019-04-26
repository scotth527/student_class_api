from rest_framework import serializers, status
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
import json
from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your models here. 
class Department(models.Model):
    department = models.CharField(max_length=50)

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        exclude = ()
    
class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'id')
        extra_kwargs = {"password":
                            {"write_only":True}
                            }

class TeacherSerializer(serializers.ModelSerializer):
    user=UserSerializer(required=True)
    department = DepartmentSerializer()
    class Meta:
        model = Teacher
        exclude = ()
        
class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    subject = models.CharField(max_length=300)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
        
class CourseSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()
    class Meta:
        model = Course
        exclude = ()
        
class Students(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    birthday = models.DateField(auto_now=False, auto_now_add=False)
    schedule = models.ManyToManyField(
        Course,
        blank=True,
    )
    image = models.CharField(max_length=1000, default="https://images.gr-assets.com/books/1388190055l/10048834.jpg")
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    class Meta: 
        verbose_name_plural = "Students"

class StudentsSerializer(serializers.ModelSerializer):
    schedule = CourseSerializer(many=True)
    user=UserSerializer(required=True)
    class Meta:
        model = Students
        exclude = ()

        

        

# class Contact(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
    

# class ContactSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Contact
#         exclude = ()

    



