from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
class User(AbstractUser):
    group = models.CharField(max_length=100, blank=True, null=True)
    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        related_name='myapp_user_groups',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        related_name='myapp_user_permissions',
        related_query_name='user',
    )
class Patients(models.Model):
    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]
    BLOOD_TYPE_CHOICES = [ 
        ('A+', 'A+'),
        ('A-', 'A-'),    
        ('B+', 'B+'),    
        ('B-', 'B-'),    
        ('AB+', 'AB+'),    
        ('AB-', 'AB-'),    
        ('O+', 'O+'),    
        ('O-', 'O-')
        ] 

    
    name = models.CharField(max_length=255)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=255)
    blood_group = models.CharField(max_length=3,choices=BLOOD_TYPE_CHOICES)
    allergies = models.TextField(blank=True)
    Medical_Surgical_History = models.TextField(blank=True)


    def __str__(self):
        return f"{self.name}"
    
class DrugsPharmacy(models.Model):

    drug_name = models.CharField(max_length=100)
    purpose = models.CharField(max_length=500)
    expiry_date = models.DateField()
    stock = models.IntegerField()

    def __str__(self):
        return f"{self.drug_name} (ID: {self.pk})"

    def formatted_expiry_date(self):
        return self.expiry_date.strftime('%m/%Y')
class TestResult(models.Model):
    PATIENT_GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ]
    TEST_TYPE_CHOICES = [
        ('Blood Test', 'Blood Test'),
        ('MRI', 'MRI'),
        ('XRAY', 'X-Ray')
    ]
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE)
    test_type = models.CharField(max_length=10, choices=TEST_TYPE_CHOICES)
    lab_result_notes = models.TextField()
    medical_image = models.FileField(upload_to='test_results/')
    def __str__(self):
        return f"{self.patient.name} ({self.patient.pk})"
    
class Consultations(models.Model):
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE)
    doctor = models.CharField(max_length=255)
    blood_pressure = models.CharField(max_length=255)
    temperature = models.CharField(max_length=255)
    weight = models.CharField(max_length=255)
    height = models.CharField(max_length=255)
    visual_exam = models.TextField(blank=True)
    physical_exam = models.TextField(blank=True)
    other_notes = models.TextField(blank=True)
    symptoms = models.TextField(blank=True)
    diagnosis = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Consultation for {self.patient} by {self.doctor}"