from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Index page")

def patientConsult(request):
    return HttpResponse("Patient consultation page")

def inventory(request):
    return HttpResponse("Inveotry page")

def profile(request):
    return HttpResponse("Profile Page")

def staff(request):
    return HttpResponse("Staff page")