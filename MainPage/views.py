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
		machine_no = Machine.objects.get(machine_no= request.POST.get("machine_no"))
		# print(machine_no.date,"===0")
		totaldt = DateSubtract(machine_no.date)
		# machine_no.Machine = Machine.objects.get(machine_no= request.POST.get("machine_no"))
		# McRecordingArea(data = serializer.data)
		# machine_no.remarks = request.POST.get("remarks")
		# print('before serializer=========', machine_no)
		# machine_no.data = request.POST
		# serializer = McRecordingAreaSerializer(machine_no, request.POST)
		# # print('before serializer=========', serializer.data)
		# if serializer.is_valid():
			# e = McRecordingArea(serializer.data)
		dat= McRecordingArea(
				root_cause		 = request.POST.get("root_cause"),
				action_taken	 = request.POST.get("action_taken"),
				remarks			 = request.POST.get("remarks"),
				total_down_time = totaldt,
				machine = Machine.objects.get(machine_no= request.POST.get("machine_no")),
				)
			# n = serializer.cleaned_data
			# t =McRecordingArea(data = serializer.data)
		dat.save()
		print('valid serializer ========')

	else:
		print('invalid serializer')	
		      #  ls = Machine.objects.get(machine_no= request.POST.get("machine_no"))
        # # print(machine_no.date,"===0")
        # # machine_no.total_down_time = DateSubtract(machine_no.date)
        # ls.total_down_time = DateSubtract(ls.date)
        # serializer = McRecordingAreaSerializer(ls, request.POST)
        
        # if serializer.is_valid():
        #     data= serializer.data
        #     print(data, "=================")

        #     ls.mcrecordingarea_set.create(serializer.data)
        #     # ls.save(force_insert=True)
        #     print('completed', "=================")
        # else:
        #     print('invalid', "=================")
		# print(dt_object2, "=================")
		# print(request.POST)
	return render(request, 'facemask/home.html',{'form':form})	


def machineshop(request):
	return render(request, 'machineshop/home.html',{})

def completed(request):
	form = DowntimeReport()
	if request.method == "POST":
		return render(request, 'facemask/home.html',{'form':form})
	
	
	return render(request, 'facemask/home.html',{'form':form})
