# Generated by Django 4.1.4 on 2023-04-25 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_remove_patients_medical_surgical_history_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultations',
            name='diagnosis',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='consultations',
            name='symptoms',
            field=models.TextField(blank=True),
        ),
    ]
