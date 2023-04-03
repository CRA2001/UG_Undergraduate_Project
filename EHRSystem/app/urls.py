from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('login/',views.loginPage,name='login'),
    path('register/',views.registerUser,name='register'),
    path('logout/',views.logoutUser,name='logout'),
    path('',views.index,name='mainpage'),
    path('patientList/',views.patientList,name='patientList'),
    path('create-patient/',views.createPatient,name='createPat'),
    path('viewMedHist/<str:pk>',views.viewMedHist,name='viewMedHist'),
    path('delete-patient/<str:pk>',views.deletePatients,name='deletePatient'),
    path('profile/',views.profile,name='profile'),
    path('staff/',views.staff,name='staff'),
    path('pharmacy_stock/',views.pharmacyStock,name='pharmacy'),
    path('create-Inv/',views.createInv, name='createInv'),
    path('update-Inv/<str:pk>/',views.updateInv, name='updateInv'),
    path('delete-Inv/<str:pk>/',views.deleteInv, name='deleteInv'),    
    path('admin/',admin.site.urls)
]