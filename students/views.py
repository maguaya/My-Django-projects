from django.shortcuts import redirect
from django.shortcuts import render
from .forms import StudentsForm
from .models import Students
from django.shortcuts import redirect



def add_student(request):
	if request.method=="POST":
		form=StudentsForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect("list_students")
	else:
		form=StudentsForm()
	return render(request,"add_student.html",{"form":form})

def list_students(request):
	students= Students.objects.all()
	return render(request,"list_students.html",{"students":students})


def student_detail(request,pk):
	student=Students.objects.get(pk=pk)
	return render(request,"student_detail.html",{"student":student})


def edit_student(request,pk):
	student=Students.objects.get(pk=pk)
	if request.method=="POST":
		form=StudentsForm(request.POST,instance=student)
		if form.is_valid():
			form.save()
		return redirect("list_students")
	else:
		form=StudentsForm(instance=student)
	return render(request,"edit_student.html",{"form":form})



			

		
	

