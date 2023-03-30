from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('login/',views.loginPage,name='login'),
    path('register/',views.registerUser,name='register'),
    path('logout/',views.logoutUser,name='logout'),
    path('',views.index,name='mainpage'),
    path('patientConsult/',views.patientConsult,name='patientConsultation'),
    path('inventory/',views.inventory,name="inventory"),
    path('profile',views.profile,name='profile'),
    path('staff/',views.staff,name='staff'),
    path('pharmacy_stock/',views.pharmacyStock,name='pharmacy'),
    path('admin/',admin.site.urls)
]