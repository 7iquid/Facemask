from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone

from api.models import Machine ,McRecordingArea, McDailyRecordingArea
from .forms import DowntimeReport
from api.serializers import MachineSerializer, McRecordingAreaSerializer

from datetime import datetime
# from pprint import pprint
import pprint
from __commandfile.objko import DateSubtract



def home(request):

	return render(request, "main/home.html" )

def facemask(request):
	form = DowntimeReport()
	# ddate = datetime.now().date()
	# # ddate =	datetime(ddate)

	if request.method == "GET":
		dbdaily10pcs = McRecordingArea.objects.all()
		# stuff.insert(0, dbdaily10pcs)
		# pprint.pprint(stuff)
		# print(dbdaily10pcs)
		# pp = pprint.PrettyPrinter(indent=4)
		# pprint.pprint(dbdaily10pcs)
		for i in dbdaily10pcs:
			pprint.pprint(i)
			
		return render(request, 'facemask/home.html',{'form':form,})

	if request.method == "POST":
		ddate = McDailyRecordingArea.objects.get(dailydate=datetime.now().date())
		if not ddate:
			ddate = McDailyRecordingArea(dailydate=ddate )
			ddate.save()
		machine_no = Machine.objects.get(machine_no= request.POST.get("machine_no"))
		totaldt = DateSubtract(machine_no.date)

		dat= McRecordingArea(
				root_cause		 = request.POST.get("root_cause"),
				action_taken	 = request.POST.get("action_taken"),
				remarks			 = request.POST.get("remarks"),
				total_down_time = totaldt,
				machine = Machine.objects.get(machine_no= request.POST.get("machine_no")),
				dalydate = ddate
				)
		dat.save()

		data = {
		'machine_no': request.POST.get("machine_no"),
		'machine_status': True
		}
		serializer = MachineSerializer(machine_no, data)
		if serializer.is_valid():
			serializer.save()
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
