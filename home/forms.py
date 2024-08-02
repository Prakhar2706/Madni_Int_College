from django import forms
from admission.models import Admission_Form
class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Admission_Form
        fields = '__all__'