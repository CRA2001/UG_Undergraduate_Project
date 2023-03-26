from django.shortcuts import render, redirect
from .models import Patients
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
patientDetails = Patients.objects.all()


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'User does not exist')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request,user)
            return redirect('mainpage')
        else:
            messages.error(request,'Username OR password does not exist.')

    context = {}
    return render(request,'app/login_register.html', context)

def index(request):
    return render(request,'app/mainpage.html')

def patientConsult(request):
    context = {'patients':patientDetails}
    return render(request,'app/patientConsult.html',context)



def inventory(request):
    return render(request,'app/inventory.html')


def profile(request):
    return render(request,'app/profile.html')


def staff(request):
    return render(request,'app/staff.html')