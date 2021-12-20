from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone

from api.models import Machine ,McRecordingArea
from .forms import DowntimeReport
from api.serializers import McRecordingAreaSerializer

from datetime import datetime
from __commandfile.objko import DateSubtract

def home(request):

	return render(request, "main/home.html" )

def facemask(request):
	form = DowntimeReport()
	if request.method == "GET":
		return render(request, 'facemask/home.html',{'form':form})

	if request.method == "POST":
		data = request.POST

		machine_no = Machine.objects.get(machine_no= request.POST.get("machine_no"))
		# print(machine_no.date,"===0")
		# machine_no.total_down_time = DateSubtract(machine_no.date)
		data.total_down_time = DateSubtract(machine_no.date)
		# a= McRecordingArea(machine_no, request.POST)
		# machine_no.remarks = request.POST.get("remarks")
		# print('before serializer=========', machine_no)
		# serializer = McRecordingAreaSerializer(a, request.POST)
		# print('before serializer=========', serializer.data)
		# if serializer.is_valid():
		# 	# n = serializer.cleaned_data
		# 	# t =McRecordingArea(data = serializer.data)
		# 	serializer.save()
		# 	print('valid serializer',serializer.data)

		# else:
		# 	print('invalid serializer')	
		
		# print(dt_object2, "=================")
		# print(request.POST)
		print('valid serializer==========', data)
		form = DowntimeReport(data)
		if form.is_valid():
			make = form.save()
			print('valid serializer', data)	
		else:
			print('invalid serializer', data)

		return render(request, 'facemask/home.html',{'form':form})	


def machineshop(request):
	return render(request, 'machineshop/home.html',{})

def completed(request):
	form = DowntimeReport()
	if request.method == "POST":
		return render(request, 'facemask/home.html',{'form':form})
	
	
	return render(request, 'facemask/home.html',{'form':form})
