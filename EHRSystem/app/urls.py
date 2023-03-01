from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('patientConsult/',views.patientConsult,name='Patient_Consultation'),
    path('inventory/',views.inventory,name="inventory"),
    path('profile',views.profile,name='profile'),
    path('staff/',views.staff,name='staff'),
    path('admin/',admin.site.urls)
]