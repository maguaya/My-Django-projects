from django.test import TestCase
from .models import Teacher
import datetime
from teacher.forms import TeacherForm
from django.test import Client
from django.urls import reverse

# class AddTeacherTestCase(TestCase):
#    def setUp(self):
#        self.data={"first_name":"Nyandia",
#        "last_name":"Kamawe",
#        "teacher_hour":"datetime.date(2019,2,1)",
#        "gender":"female",
#        "staff_number":"1234",
#        "email":"nyandia@gmail.com",
#        "contact":"+254743696424",
#        "date_employed":"datetime.date.today()",
#        }
#        self.bad_data={"first_name":"Nyandia",
#        "last_name":"Kamawe",
#        "teacher_hour":"datetime.date(2019,2,1)",
#        "gender":"female",
#        "staff_number":"2254",
#        "email":"antor20",
#        "contact":"+254743675424",
#        "date_employed":"datetime.date.today()",
#        }
#    def test_tutor_form_accepts_valid_data(self):
#        form = TutorForm(self.data)
#        self.assertFalse(form.is_valid())
#    def test_tutor_form_rejects_invalid_data(self):
#        form = TutorForm(self.bad_data)
#        self.assertFalse(form.is_valid())
#    def test_add_tutor_view(self):
#        client=Client()
#        url=reverse("add_tutor")
#        response=client.post(url,self.data)
#        self.assertEqual(response.status_code,200)
#    def test_add_tutor_view(self):
#        client = Client()
#        url = reverse("add_tutor")
#        response=client.post(url,self.bad_data)
#        self.assertEqual(response.status_code,400)

# return HttpResponse("invalid data",status=400)


