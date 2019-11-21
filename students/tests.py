
from django.test import TestCase
from .models import Students
from .forms import StudentsForm
import datetime
from django.test import Client


class Students_TestCase(TestCase):

    def setUp(self):
        self.student = Students(
        first_name="LEAH",
        last_name="OUMA",
        date_of_birth=datetime.date(1996,9,27),
        registration_number="12345",
        email="leahatienoouma@gmail.com",
        phone_number="0700182857",
        gender="Female",
        date_joined=datetime.date.today(),)
        

    def test_full_name_contains_first_name(self):
        self.assertIn(self.student.first_name, self.student.full_name())
    def test_full_name_contains_last_name(self):
        self.assertIn(self.student.last_name, self.student.full_name())

class CreateStudentsTestCase(TestCase):
    def SetUp(self):

            self.data = {"first_name": "LEAH",
                         "last_name":"OUMA",
                         "date_of_birth":datetime.date(1996,9,27),
                         "registration_number":"12345",
                         "email":"leahatienoouma@gmail.com",
                         "phone_number":"0700182857",
                         "guardian_number":"0719555159",
                         "id_name":"998765",

      }
            self.bad_data = {"first_name": "LEAH",
                             "last_name":"OUMA",
                             "date_of_birth":datetime.date(1999,9,27),
                             "registration_number":"2345",
                             "email":"leahotienoouma@gmail.com",
                             "phone_number":"0700282857",
                             "guardian_number":"0729555159",
                             "id_name":"339867",

      }


    def test_students_form_accepts_valid_data(self):
        form =StudentsForm(self.data)
        self.assertTrue(form.is_valid())

        def test_add_studen_view_rejects_invalid_bad_data(self):
            Client=Client()
            url=reverse("add_student")
            request=client.post(url,self.data)
            self.assertEqual(request.status_code,200)

             def test_add_studen_view_rejects_invalid_bad_data(self):
            Client=Client()
            url=reverse("add_student")
            request=client.post(url,self.data)
            self.assertEqual(request.status_code,400)
            
      
            
      


    def test_age_above_18(self):
       self.assertFalse(self.student.clean() < 18)
    def test_age_below_30(self):
       self.assertFalse( self.student.clean() > 30)