from students.models import Students
from teacher.models import Teacher
from course.models import Course
from rest_framework import serializers

class StudentsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Students
		fields ="__all__"


class TeacherSerializer(serializers.ModelSerializer):
	class Meta:
		model = Teacher
		fields ="__all__"

class CourseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Course
		fields ="__all__"
	
		
 		 