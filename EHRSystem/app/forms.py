from django.forms import ModelForm
from .models import DrugsPharmacy,Patients,TestResult
from django import forms
from django.contrib.auth import  get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, User

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

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'group']