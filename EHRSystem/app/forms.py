from django.forms import ModelForm
from .models import DrugsPharmacy,Patients,TestResult
from django import forms
from django.contrib.auth import  get_user_model

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

class addStaffForm(ModelForm):
    class Meta:
        model = get_user_model()
        fields = '__all__'
