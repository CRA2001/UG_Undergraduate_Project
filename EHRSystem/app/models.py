from django.db import models
from django.contrib.auth.models import User


class Patients(models.Model):
    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]
    
    name = models.CharField(max_length=255)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    ethnicity = models.CharField(max_length=255)
    blood_group = models.CharField(max_length=10)
    allergies = models.TextField(blank=True)
    medicalHist_conditions = models.TextField(blank=True)
    medicalHist_pastSurgery = models.TextField(blank=True)
    medicalHist_mental = models.TextField(blank=True)
    medicalHist_medication = models.TextField(blank=True)
    medicalHist_sexual = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} (ID: {self.pk})"
    