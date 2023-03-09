from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('',views.index,name='mainpage'),
    path('patientConsult/',views.patientConsult,name='patientConsultation'),
    path('inventory/',views.inventory,name="inventory"),
    path('profile',views.profile,name='profile'),
    path('staff/',views.staff,name='staff'),
    path('admin/',admin.site.urls)
]