from django.test import TestCase
from students.models import Students
from course.models import Course
from teacher.models import Teacher
import datetime
class StudentCourseTeachersTestCase(TestCase):
    def setUp(self):
        self.students_a =Students.objects.create(
            first_name = "Virginiah",
            last_name = "Wangari",
            date_of_birth = datetime.date(2000,10,31),
            email = "vwangari@gmail.com",
            phone_number = "0712345678",
            date_joined = datetime.date.today()
            )
        self.students_b = Students.objects.create(
            first_name = "Hottensiah",
            last_name = "Wanjiku",
            date_of_birth = datetime.date(2000,12,31),
            email = "hwanjiku@gmail.com",
            phone_number = "0787654321",
            date_joined = datetime.date.today()
            )
        self.python = Course.objects.create(
            name = "python",
            duration_months = "10",
            Course_number = "1",
            description = "Learn to code in Python",
           )
        self.javascript = Course.objects.create(
            name = "javascript",
            duration_months = "6",
            Course_number = "3",
            description = "Learn to code in JavaScript",
           )
        self.hardware = Course.objects.create(
            name = "hardware",
            duration_months = "6",
            Course_number = "5",
            description = "Learn to design electronics staffs",
           )
        self.teachers_a = Teachers.objects.create(
            first_name = "Antony",
            last_name = "Orenge",
            email = "antorenge@gmail.com",
            phone_number = "+254743675424",
            date_of_birth =  datetime.date(2000,10,31),
            )
        self.teachers_b = Teachers.objects.create(
            first_name = "James",
            last_name = "Mwai",
            email = "python@gmail.com",
            phone_number = "+254743675424",
            date_of_birth =  datetime.date(2000,10,31),
            )
    def test_student_can_join_many_courses(self):
        self.assertEqual(self.student_a.courses.count(),0)
        self.student_a.courses.add(self.python)
        self.assertEqual(self.student_a.courses.count(),1)
        self.student_a.courses.add(self.javascript)
        self.assertEqual(self.student_a.courses.count(),2)
        self.student_a.courses.add(self.hardware)
        self.assertEqual(self.student_a.courses.count(),3)
    def test_course_can_have_many_students(self):
        self.python.students.add(self.student_a, self.student_b)
        self.assertEqual(self.python.students.count(),2)
    def test_teacher_can_have_many_courses(self):
        self.teachers_a.courses.add(self.javascript,self.hardware)
        self.assertEqual(self.teachers_a.courses.count(),2)
    def test_course_cannot_have_many_teachers(self):
        self.javascript.teachers = self.teachers_a
        self.assertEqual(self.python.teachers.first_name, "Antony")
        self.python.teachers = self.teachers_b
        self.assertEqual(self.python.teachers.first_name, "James")
    def test_course_teacher_is_in_student_teachers_list(self):
        self.python.teachers = self.teachers_b
        self.student_a.courses.add(self.python)
        teachers = self.student_a.teachers()
        self.assertFalse(self.teachers_b in teachers)
