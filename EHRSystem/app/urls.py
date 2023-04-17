from django.urls import path
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views


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
    path('test_results/', views.test_results, name='test_results'),
    path('add_test_result/', views.add_test_result, name='add_test_result'),
    path('update_test_result/<int:pk>/', views.update_test_result, name='update_test_result'),
    path('delete_test_result/<int:pk>/', views.delete_test_result, name='delete_test_result'),
    path('test_results/<int:pk>/download_pdf/', views.DownloadPDFView.as_view(), name='download_pdf'),
    path('staffManage/',views.staffManagement,name="staffManage"),
    path('addStaff/',views.addStaff,name='addStaff'),
    path('deleteStaff/<str:pk>',views.deleteStaff,name='deleteStaff'),
    path('updateStaff/<str:pk>',views.updateStaff,name='updateStaff'),
    path('admin/',admin.site.urls)
]