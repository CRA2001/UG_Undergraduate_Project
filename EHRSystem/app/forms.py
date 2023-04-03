from django.forms import ModelForm
from .models import DrugsPharmacy,Patients,TestResult

class PharmacyForm(ModelForm):
    class Meta:
        model = DrugsPharmacy
        fields = '__all__'

class NewPatientForm(ModelForm):
    class Meta:
        model = Patients
        fields = '__all__'
        
class TestResultForm(ModelForm):
    class Meta:
        model = TestResult
        fields = '__all__'