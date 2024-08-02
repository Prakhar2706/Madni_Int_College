from django.contrib import admin
from faculty.models import Faculty
# Register your models here.
class FacultyData(admin.ModelAdmin):
    list_display=['Faculty_name','Faculty_degree','Faculty_contact']
    ordering=('id',)
admin.site.register(Faculty,FacultyData)    

