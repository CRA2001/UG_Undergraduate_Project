# Generated by Django 4.1.4 on 2023-04-25 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_consultations_diagnosis_consultations_symptoms'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TestResult',
        ),
    ]
