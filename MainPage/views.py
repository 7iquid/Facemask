from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from api.models import Machine

def home(request):

	return render(request, "main/home.html" )

def facemask(request):
	machine_data = Machine.objects.get(id="1")
	machine_data = machine_data.date
	# print("--------------------------------->")
	return render(request, 'facemask/home.html',{'machine_data':machine_data})
