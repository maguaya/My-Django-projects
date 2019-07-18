from django.shortcuts import render
from students.models import Students
from .serializers import StudentsSerializer
from teacher.models import Teacher
from .serializers import TeacherSerializer
from course.models import Course
from .serializers import CourseSerializer
from rest_framework import viewsets

class StudentsViewSet(viewsets.ModelViewSet):
	queryset = Students.objects.all()
	serializer_class = StudentsSerializer

class TeacherViewSet(viewsets.ModelViewSet):
	queryset = Teacher.objects.all()
	serializer_class = TeacherSerializer


class CourseViewSet(viewsets.ModelViewSet):
	queryset = Course.objects.all()
	serializer_class = CourseSerializer

