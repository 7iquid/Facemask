from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from api.models import Machine ,McRecordingArea
from .forms import DowntimeReport

from datetime import datetime

def home(request):

	return render(request, "main/home.html" )

def facemask(request):
	form = DowntimeReport()
	if request.method == "GET":
		return render(request, 'facemask/home.html',{'form':form})

	if request.method == "POST":
		date1 = Machine.objects.get(machine_no= request.POST.get("machine_no"))
		date2 = date1.date
		now = datetime.now()
		timebefore = datetime.timestamp(date2)
		timeafter =  datetime.timestamp(now)

		dt_object = (timeafter - timebefore)
		# timestamp = 1545730073
		dt_object = datetime.fromtimestamp(dt_object)
		a_timedelta = dt_object - datetime(1970, 1, 1)
		seconds = a_timedelta.total_seconds()
		h = seconds//3600

		# dt_object3 = datetime.strptime(date2, "%d/%m/%Y %H:%M:%S")
		# dt_object4 = datetime.strptime(now, "%d/%m/%Y %H:%M:%S")
		# dt_object5 = dt_object4-dt_object3

		# dt_object = datetime.fromtimestamp(totaldt)
		# dt_object = totaldt/1000
		# totaldt2 = now-date2
		# dt_object2 = datetime.fromtimestamp(totaldt2)

		print(type(h),h, "=================")
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
