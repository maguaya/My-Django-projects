from django.db import models
class Teacher(models.Model):
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	date_of_birth=models.DateField()
	gender=models.CharField(max_length=20)
	registation_number=models.CharField(max_length=20)
	email=models.EmailField(max_length=70)
	phone_number=models.CharField(max_length=30)
	date_joined =models.DateField()
	def __str__(self):
		return self.first_name+" "+self.last_name


	