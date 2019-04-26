from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns = [
    # path('contacts/<int:contact_id>', views.ContactsView.as_view(), name='id-contacts'),
    # path('contacts/', views.ContactsView.as_view(), name='all-contacts'),
    path('students/', views.StudentsView.as_view(), name='all-students'),
    path('students/<int:student_id>', views.StudentsView.as_view(), name='student'),
    path('teachers/', views.TeacherView.as_view(), name='all-teachers'),
    path('teachers/<int:teacher_id>', views.TeacherView.as_view(), name='teacher'),
    path('courses/', views.CourseView.as_view(), name='all-course'),
    path('courses/<int:course_id>', views.CourseView.as_view(), name='course'),
    path('department/<int:dept>', views.DeptView.as_view(), name='courses-by-department')
   
    
]
