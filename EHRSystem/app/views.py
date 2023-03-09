from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'app/mainpage.html')

def patientConsult(request):
    return render(request,'app/patientConsult.html')

def inventory(request):
    return render(request,'app/inventory.html')

def profile(request):
    return render(request,'app/profile.html')

def staff(request):
    return render(request,'app/staff.html')