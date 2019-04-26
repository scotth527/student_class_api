from django.shortcuts import render
import json
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Students, Teacher, Course
from api.models import TeacherSerializer, StudentsSerializer, CourseSerializer, UserSerializer
# from api.models import Contact, ContactSerializer


class StudentsView(APIView):
    def get(self, request, student_id=None):
        
        if student_id is not None:
            student = Students.objects.get(id=student_id)
            serializer = StudentsSerializer(student, many=False)
            return Response(serializer.data)
        else:
            students = Students.objects.all()
            serializer = StudentsSerializer(students, many=True)
            return Response(serializer.data)
            
    def patch(self, request, student_id=None):
        if student_id is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                student = Students.objects.get(id=student_id)
            except Students.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
                
            serializer = StudentsSerializer(student, data=request.data, partial=True)
            
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, student_id=None):
        if student_id is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                student = Students.objects.get(id=student_id)
            except Students.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
                
            student.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
            
            
class TeacherView(APIView):
    def get(self, request, teacher_id=None):
        
        if teacher_id is not None:
            teacher = Teacher.objects.get(id=teacher_id)
            serializer = TeacherSerializer(teacher, many=False)
            return Response(serializer.data)
        else:
            teachers = Teacher.objects.all()
            serializer = TeacherSerializer(teachers, many=True)
            return Response(serializer.data)
            
    def delete(self, request, teacher_id=None):
        if teacher_id is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                teacher = Teacher.objects.get(id=teacher_id)
            except Teacher.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
                
            teacher.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
            
    def patch(self, request, teacher_id=None):
        if teacher_id is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                teacher = Teacher.objects.get(id=teacher_id)
            except Course.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
                
            serializer = TeacherSerializer(teacher, data=request.data, partial=True)
            
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CourseView(APIView):
    def get(self, request, course_id=None):
        if course_id is not None:
            course = Course.objects.get(id=course_id)
            serializer = CourseSerializer(course, many=False)
            return Response(serializer.data)
        else:
            courses = Course.objects.all()
            serializer = CourseSerializer(courses, many=True)
            return Response(serializer.data)
    
    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    def delete(self, request, course_id=None):
        if course_id is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                course = Course.objects.get(id=course_id)
            except Course.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
                
            course.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
            
    def patch(self, request, course_id=None):
        if course_id is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                course = Course.objects.get(id=course_id)
            except Course.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
                
            serializer = CourseSerializer(course, data=request.data, partial=True)
            
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
class DeptView(APIView):
    def get(self, request, dept=None):
        if dept is None:
             return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                courses = Course.objects.filter(department_id__exact=dept)
            except Course.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
                
        if courses is not None:
            serializer = CourseSerializer(courses, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
            
class TeacherDeptView(APIView):
    def get(self, request, dept=None):
        if dept is None:
             return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                teachers = Teacher.objects.filter(department_id__exact=dept)
            except Course.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
                
        if teachers is not None:
            serializer = TeacherSerializer(teachers, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
            
        

# class ContactsView(APIView):
#     def get(self, request, contact_id=None):

#         if contact_id is not None:
#             contact = Contact.objects.get(id=contact_id)
#             serializer = ContactSerializer(contact, many=False)
#             return Response(serializer.data)
#         else:
#             contacts = Contact.objects.all()
#             serializer = ContactSerializer(contacts, many=True)
#             return Response(serializer.data)
        
#     def post(self, request):
            
#         serializer = ContactSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        
#     def delete(self, request, contact_id):
        
#         contact = Contact.objects.get(id=contact_id)
#         contact.delete()
        
#         return Response(status=status.HTTP_204_NO_CONTENT)
        
