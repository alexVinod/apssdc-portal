from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as dj_login,logout as dj_logout

from django.core.mail import send_mail

from .models import Job,Update,Acheivement,Director, DistrictOfficer, Gallery
# Create your views here.

def home(request):
	jobs = Job.objects.filter(status='active')
	for job in jobs:
		print(job.status)
	updates = Update.objects.all()
	acheivements = Acheivement.objects.all()

	context={"jobs":jobs,'updates':updates,'acheivements':acheivements}
	return render(request,"home.html",context)

def aboutUs(request):
	return render(request,"aboutus.html")

def boardDirectors(request):
	directors = Director.objects.all()
	context = {"directors": directors}
	return render(request,"boarddirectors.html",context)

def comingSoon(request):
	return render(request,"comingSoon.html")

def careers(request):
	return render(request,"careers.html")

def gallery(request):
	gallerys = Gallery.objects.all()
	return render(request,"gallery.html",{'gallerys':gallerys})	

def contact(request):
	officers = DistrictOfficer.objects.all()
	return render(request,"contract.html",{'officers':officers})