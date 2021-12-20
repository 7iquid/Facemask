from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from api.models import Machine ,McRecordingArea
from .forms import DowntimeReport

def home(request):

	return render(request, "main/home.html" )

def facemask(request):
	if request.method == "GET":
		form = DowntimeReport()
		return render(request, 'facemask/home.html',{'form':form})

	if request.method == "POST":
		# form = DowntimeReport()
		print(request.POST)
		return render(request, 'facemask/home.html',{'form':form})	


def machineshop(request):
	return render(request, 'machineshop/home.html',{})

def completed(request):
	form = DowntimeReport()
	if request.method == "POST":
		return render(request, 'facemask/home.html',{'form':form})
	
	
	return render(request, 'facemask/home.html',{'form':form})
