from django.db import models
from teacher.models import Teacher
	
class Course(models.Model):
	name=models.CharField(max_length=50)
	duration_months=models.IntegerField(max_length=250)
	Course_number=models.CharField(max_length=50)
	description=models.TextField()
	teacher=models.ForeignKey(Teacher,on_delete=models.PROTECT,default=True)
	def __str__(self):
		return self.name
	
	
		
		
