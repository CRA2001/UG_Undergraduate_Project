from django.shortcuts import render, redirect, get_object_or_404
from django.http import FileResponse
import io
from .models import Patients, DrugsPharmacy, TestResult, Consultations
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .forms import PharmacyForm,NewPatientForm,TestResultForm,addStaffForm
patientDetails = Patients.objects.all()
drugDetails = DrugsPharmacy.objects.all()
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.db.models import Q

#Login page
def loginPage(request):
    page = 'login'
    #if login is sucssessful go to the mainpage
    if request.user.is_authenticated:
        return redirect('mainpage')
    # a POST http method is sent via request 
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

#Display the list of patients
@login_required(login_url='/login')
def patientList(request):
    #query for the searchbar 
    query = request.GET.get('q')
    if(query):
        #filtering based on the search with is either the name, email or phone of a patient
        patients = Patients.objects.filter(
            Q(name__icontains=query) |
            Q(email__icontains=query) |
            Q(phone__icontains=query) 
        )
    else:
        patients = Patients.objects.all()
    context = {'patients':patients}
    return render(request,'app/patientList.html',context)

#creating a new patient.
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
#deleting a patient record
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

#Displaying the list of drugs and antibiotics etc, as well as allowing to search through them.
@login_required(login_url='/login')
def pharmacyStock(request):
    query = request.GET.get('q')
    if query:
        drugs = DrugsPharmacy.objects.filter(
            Q(drug_name__icontains=query) |
            Q(purpose__icontains=query)
        )
    else:
        drugs = DrugsPharmacy.objects.all() 
    context = {'drugs':drugs}
    return render(request,'app/pharmacyStock.html',context)

#View for adding a new drug or antibiotic
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

#updating the stock of the pharmacy item
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

#Test Results section

#Displaying the list of test results in the form of a list
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

#Allowing the user to update the test results 
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

#Allowing the user to delete the test result
def delete_test_result(request, pk):
    result = TestResult.objects.get(id=pk) 
    if request.method == 'POST':
        result.delete()
        return redirect('test_results')
    return render(request,'app/delete.html',{'obj':result})

#this class downloads the pdf of the medical image.
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
    
#this will access all the users from the user model and output them all in the form of a list
def staffManagement(request):
    users = get_user_model().objects.all()
    context = {'users':users}
    return render(request,'app/staffmanage.html',context)

# this will add new staff
@login_required(login_url='/login')    
def addStaff(request):
    form = addStaffForm()
    if request.method == 'POST':
        form = addStaffForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('staffManage')
    context = {'form':form}
    return render(request,'app/addStaff.html',context)

#this will delete the staff 
def deleteStaff(request,pk):
    staff = get_user_model().objects.get(id=pk)
    if request.method == 'POST':
        staff.delete()
        return redirect('staffManage')
    return render(request,'app/delete.html',{'obj':staff})

#This updates the details of the staff listings
def updateStaff(request,pk):
    user = get_user_model().objects.get(id=pk)
    initial_data = {'username':user.username,'email':user.email,'forename':user.first_name,'surname':user.last_name,'date':user.date_joined,'groups':user.groups.all()}
    form = addStaffForm(initial=initial_data)
    if request.method == "POST":
        form = addStaffForm(request.POST, instance=user)
        if  form.is_valid():
            form.save()
            return redirect('pharmacy')
    context = {'form':form}
    return render(request,'app/addStaff.html',context)

#patientCconsultationPg1 refers to the first page of the consultation feature 
def patientConsultationPg1(request):
    # query is used for the searchbar which will search based
    # on the id and the name of the search value inputted in 
    # the searchbar
    query = request.GET.get('q')
    if query:
        # the search will pertain to the id or the name of the patient.
        patients = Patients.objects.filter(
            Q(id__icontains=query)|
            Q(name__icontains=query)
        )
    else:
    # if the query value(search value) is doesn't exist then just output all
        patients = Patients.objects.all()
    context = {'patients':patients}
    return render(request,'app/patConsult1.html',context)

#patientConsultationPg2 refers to the second page of the consultation feature
def patientConsultationPg2(request, pk):
    patient = Patients.objects.get(id=pk)
    if request.method == 'POST':
        doctor = f"{request.user.first_name} {request.user.last_name}"

        # Save the consultation form data to the database
        consultation = Consultations.objects.create(
            patient=patient,
            doctor=doctor,
            blood_pressure=request.POST.get('blood_pressure'),
            temperature=request.POST.get('temperature'),
            weight=request.POST.get('weight'),
            height=request.POST.get('height'),
            visual_exam=request.POST.get('visual_exam'),
            physical_exam=request.POST.get('physical_exam'),
            other_notes=request.POST.get('other_notes'),
        )

        # Redirect to the success page
        return redirect('patient_consult_success', consultation_id=consultation.id)

    context = {
        'patient': patient
    }
    return render(request,'app/patConsult2_form.html',context)

# This view will displays a success screen which indicates that the form has been successfully filled out
def patientConsultationSuccess(request, consultation_id):
    consultation = Consultations.objects.get(id=consultation_id)
    context = {
        'consultation': consultation
    }
    return render(request, 'app/patConsult_success.html', context)


def patient_detail(request, pk):
    patient = get_object_or_404(Patients, id=pk)
    consultations = patient.consultations_set.all().order_by('-date_created')

    context = {
        'patient': patient,
        'consultations': consultations
    }
    return render(request, 'app/patient_detail.html', context)

#consultation_list refers to the list of consultation forms
def consultation_list(request):
    consForms = Consultations.objects.all()
    context= {'Consultations':consForms}
    return render(request,"app/PatconsultationForms_List.html",context)
