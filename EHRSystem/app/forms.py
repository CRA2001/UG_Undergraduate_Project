from django.forms import ModelForm
from .models import DrugsPharmacy,Patients

class PharmacyForm(ModelForm):
    class Meta:
        model = DrugsPharmacy
        fields = '__all__'

class NewPatientForm(ModelForm):
    class Meta:
        model = Patients
        fields = '__all__'
        
