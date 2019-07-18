from django.contrib import admin
from .models import Course


class CourseAdmin(admin.ModelAdmin):
	list_display=("name","Course_number", "duration_months", "description")
	search_fields=("name","Course_number", "duration_months", "description")
	# list_filter=("date_joined","date_of_birth")
admin.site.register(Course,CourseAdmin)



