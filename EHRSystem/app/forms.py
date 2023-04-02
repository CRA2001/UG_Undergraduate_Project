from django.forms import ModelForm
from .models import DrugsPharmacy

class PharmacyForm(ModelForm):
    class Meta:
        model = DrugsPharmacy
        fields = '__all__'