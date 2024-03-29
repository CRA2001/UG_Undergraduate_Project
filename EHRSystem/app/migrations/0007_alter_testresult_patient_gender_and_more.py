# Generated by Django 4.1.4 on 2023-04-03 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_testresult'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testresult',
            name='patient_gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='test_type',
            field=models.CharField(choices=[('Blood Test', 'Blood Test'), ('MRI', 'MRI'), ('XRAY', 'X-Ray')], max_length=10),
        ),
    ]
