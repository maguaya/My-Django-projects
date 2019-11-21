from django.db import models
from course.models import Course
import datetime
from django.core.exceptions import ValidationError
    # Create your models here.
class Students(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    date_of_birth=models.DateField()
    gender=models.CharField(max_length=20)
    registration_number=models.CharField(max_length=20)
    email=models.EmailField(max_length=70)
    phone_number=models.CharField(max_length=30)
    date_joined =models.DateField()
    image=models.ImageField(upload_to="profile_image",blank=True)
    courses=models.ManyToManyField(Course)
    
    def __str__(self):
        return self.first_name+" "+self.last_name

    def full_name(self):
        return "{} {}".format(
            self.first_name,
            self.last_name
            )

def get_age(self):
    today = datetime.date.today()
    return today.year-self.date_of_birth.year
    age = property(get_age)

def clean(self):
    age=self.age
    if age <18 or age>30:
     raise ValidationError("you need to be above 18 and below 30")
    return age
