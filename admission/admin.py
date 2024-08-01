from django.contrib import admin
from admission.models import Admission_Form
# Register your models here.

class AdmissionAdmin(admin.ModelAdmin):
    list_display=['Full_Name','Class']
    ordering = ('id',)

admin.site.register(Admission_Form,AdmissionAdmin)
   