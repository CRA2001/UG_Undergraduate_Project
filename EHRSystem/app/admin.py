from django.contrib import admin
from app.models import Patients,DrugsPharmacy,TestResult
# Register your models here.
admin.site.register(Patients)
admin.site.register(DrugsPharmacy)
admin.site.register(TestResult)