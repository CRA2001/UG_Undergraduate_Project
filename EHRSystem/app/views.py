from django.shortcuts import render, redirect
from .models import Patients, DrugsPharmacy
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

patientDetails = Patients.objects.all()
drugDetails = DrugsPharmacy.objects.all()


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('mainpage')   
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
    context = {'page':page}
    return render(request,'app/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('mainpage')

def registerUser(request):
    page = 'register'
    return  render(request,'app/login_register.html')

@login_required(login_url='/login')
def index(request):
    return render(request,'app/mainpage.html')

@login_required(login_url='/login')
def patientConsult(request):
    context = {'patients':patientDetails}
    return render(request,'app/patientConsult.html',context)

@login_required(login_url='/login')
def inventory(request):
    return render(request,'app/inventory.html')

@login_required(login_url='/login')
def profile(request):
    return render(request,'app/profile.html')


@login_required(login_url='/login')
def staff(request):
    return render(request,'app/staff.html')

@login_required(login_url='/login')
def pharmacyStock(request):
    context = {'drugs':drugDetails}
    return render(request,'app/pharmacyStock.html',context)