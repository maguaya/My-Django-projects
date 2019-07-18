from django.contrib import admin

from .models import Teacher
admin.site.register(Teacher)



# class TeacherAdmin(admin.ModelAdmin):
# 	list_display=("first_name","last_name","registration_number","date_joined","email","image")
# 	search_fields=("email","first_name","registration_number")
# 	# list_filter=("date_joined","date_of_birth"
# admin.site.register(Teacher,TeacherAdmin)


