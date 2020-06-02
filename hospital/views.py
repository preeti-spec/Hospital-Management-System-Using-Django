from django.shortcuts import render,redirect
from .models import*
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth import authenticate,login,logout
from .forms import SignUpForm

# Create your views here.

def About(request):
	return render(request,'about.html')


def Contact(request):
	return render(request,'contact.html')

def Home(request):
	return render(request,'home.html')

def Login(request):
	error = ""
	if request.method=='POST':
		u = request.POST['uname']
		p = request.POST['pwd']
		user = authenticate(username=u,password=p)
		try:
			if user.is_staff:
				login(request,user)
				error = "yes"
			else:
				error = "no"
		except:
			error = "no"
	d = {'error':error}
	return render(request,'login.html',d)


def Logout(request):
	if not request.user.is_staff:
		return redirect('home')
	logout(request)
	return redirect('home')


def Add_Doctor(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')

    if request.method=="POST":
        n = request.POST['name']
        c = request.POST['contact']
        s = request.POST['specialization']
        
        try:
            Doctor.objects.create(name=n,contact=c,specialization=s)
            error="no"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'add_doctor.html',d)

def View_Doctor(request):
    if not request.user.is_staff:
        return redirect('login')
        
    doc = Doctor.objects.all()
    d = {'doc':doc}
    return render(request,'view_doctor.html',d)



def Delete_Doctor(request,pid):
    if not request.user.is_staff:
        return redirect('login')
        
    doctor = Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('view_doctor')


def Add_Patient(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')

    if request.method=="POST":
        n = request.POST['name']
        c = request.POST['contact']
        a = request.POST['age']
        g = request.POST['gender']
        ad = request.POST['address']
        
        try:
            Patient.objects.create(name=n,contact=c,age=a,gender=g,address=ad)
            error="no"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'add_patient.html',d)

def View_Patient(request):
    if not request.user.is_staff:
        return redirect('login')
        
    pat = Patient.objects.all()
    d = {'pat':pat}
    return render(request,'view_patient.html',d)



def Delete_Patient(request,pid):
    if not request.user.is_staff:
        return redirect('login')
        
    patient = Patient.objects.get(id=pid)
    patient.delete()
    return redirect('view_patient')

def Add_Appointment(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()

    if request.method=="POST":
        d = request.POST['doctor']
        p = request.POST['patient']
        d1 = request.POST['date']
        t = request.POST['time']
        doctor = Doctor.objects.filter(name=d),first()
        patient = Patient.objects.filter(name=p),first()
        
        try:
            Appointment.objects.create(doctor=doctor,patient=patient,date1=date1,time1=time1)
            error="no"
        except:
            error="yes"
    d = {'doctor':doctor1,'patient':patient1,'error':error}
    return render(request,'add_appointment.html',d)

def View_Appointment(request):
    if not request.user.is_staff:
        return redirect('login')
        
    appoint = Appointment.objects.all()
    d = {'appoint':appoint}
    return render(request,'view_appointment.html',d)



def Delete_Appointment(request,pid):
    if not request.user.is_staff:
        return redirect('login')
        
    appointment= Appointment.objects.get(id=pid)
    appointment.delete()
    return redirect('view_appointment')


def Admindsh(request):
	return render(request,'admindsh.html')



def SignUp(request):
	if request.method=="POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			print("HELLO")
			print(form)
			form.save
		return redirect('home')
	else:
		form = SignUpForm()
	return render(request,'signup.html',{'form':form})



def Feedback(request):
    return render(request,'feedback.html')










































































































































