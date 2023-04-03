from django.shortcuts import render, redirect, get_object_or_404
from django.http import FileResponse
import io
from .models import Patients, DrugsPharmacy, TestResult
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .forms import PharmacyForm,NewPatientForm,TestResultForm
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

#Patients
@login_required(login_url='/login')
def patientList(request):
    context = {'patients':patientDetails}
    return render(request,'app/patientList.html',context)

@login_required(login_url='/login')    
def createPatient(request):
    form = NewPatientForm()
    if request.method == 'POST':
        form = NewPatientForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('patientList')
    context = {'form':form}
    return render(request,'app/newpatient_form.html',context)

@login_required(login_url='/login')    
def deletePatients(request,pk):
    patient = Patients.objects.get(id=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('patientList')
    return render(request,'app/delete.html',{'obj':patient})

@login_required(login_url='/login')    
def viewMedHist(request,pk):
    #drug = DrugsPharmacy.objects.get(id=pk)
    patient = Patients.objects.get(id=pk)
    context = {'patient':patient}
    return render(request,'app/viewMedHist.html',context)


#User profile
@login_required(login_url='/login')
def profile(request):
    return render(request,'app/profile.html')

#Staff
@login_required(login_url='/login')
def staff(request):
    return render(request,'app/staff.html')

#Pharmacy
@login_required(login_url='/login')
def pharmacyStock(request):
    context = {'drugs':drugDetails}
    return render(request,'app/pharmacyStock.html',context)

@login_required(login_url='/login')
def createInv(request):
    form = PharmacyForm()
    if request.method == 'POST':
        form = PharmacyForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('pharmacy')
    context = {'form':form}
    return render(request,'app/stock_form.html',context)

@login_required(login_url='/login')
def updateInv(request,pk):
    drug = DrugsPharmacy.objects.get(id=pk)
    initial_data = {'drug_name': drug.drug_name,'purpose': drug.purpose,'expiry_date': drug.expiry_date,'stock': drug.stock}
    form = PharmacyForm(initial=initial_data)
    if request.method == "POST":
        form = PharmacyForm(request.POST, instance=drug)
        if  form.is_valid():
            form.save()
            return redirect('pharmacy')
    context = {'form':form}
    return render(request,'app/stock_form.html',context)


@login_required(login_url="/login")
def deleteInv(request,pk):
    drug = DrugsPharmacy.objects.get(id=pk)
    if request.method == 'POST':
        drug.delete()
        return redirect('pharmacy')
    return render(request,'app/delete.html',{'obj':drug })

#Create Test Results sections

def test_results(request):
    test_results = TestResult.objects.all()
    return render(request, 'app/test_results.html', {'test_results': test_results})

def add_test_result(request):
    if request.method == 'POST':
        form = TestResultForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('test_results')
    else:
        form = TestResultForm()
    return render(request, 'app/add_test_result.html', {'form': form})

def update_test_result(request, pk):
    test_result = get_object_or_404(TestResult, pk=pk)
    if request.method == 'POST':
        form = TestResultForm(request.POST, request.FILES, instance=test_result)
        if form.is_valid():
            form.save()
            return redirect('test_results')
    else:
        form = TestResultForm(instance=test_result)
    return render(request, 'app/add_test_result.html', {'form': form})

def delete_test_result(request, pk):
    result = TestResult.objects.get(id=pk)
    if request.method == 'POST':
        result.delete()
        return redirect('test_results')
    return render(request,'app/delete.html',{'obj':result})

class DownloadPDFView(View):
    def get(self, request, pk):
        test_result = get_object_or_404(TestResult, pk=pk)
        pdf_file = test_result.medical_image.path
        
        # Open the PDF file and read its contents into memory
        with open(pdf_file, 'rb') as f:
            buffer = io.BytesIO(f.read())
        
        # Close the file and create a response with the PDF contents
        response = FileResponse(buffer, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{test_result.patient_name,test_result.test_type}.pdf"'
        return response