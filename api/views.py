from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import Machine
from .serializers import MachineSerializer
from django.http import JsonResponse
from django.views.generic import View

from pyfiglet import Figlet
f = Figlet(font='slant')
#/api/no

class MachineStatus(APIView):
  
    @csrf_exempt
    def get(self, request):
        data = {}
        try:
            ajax = request.GET.get('machine_no1')
            ajax2 = request.GET.get('machine_no2')
            ajax3 = request.GET.get('machine_no3')
            # print(ajax,ajax2,ajax3)
            ajax = Machine.objects.get(id=ajax)
            ajax2 = Machine.objects.get(id=ajax2)
            ajax3 = Machine.objects.get(id=ajax3)

            ajaxresponse={
                "machine_status1": ajax.machine_status,
                "machine_status2": ajax2.machine_status,
                "machine_status3": ajax3.machine_status,
            }
            print(ajaxresponse)
            return JsonResponse(ajaxresponse)
        except Exception as e: 
            try:
                machineNo = Machine.objects.all()
                serializer = MachineSerializer(machineNo, many=True)
                data = serializer.data
                print(f.renderText("Gumana na"))
                # data['status'] = True

            except Exception as e:
                data['status'] = False
                data['message'] = "Oops something went wrong"
                print(f.renderText("ayaw Gumana"))
            return Response(data=data)

    @csrf_exempt
    def put(self, request):
        data = {}
        print(type(request.data.get('machine_no')))
        try:
            machine_no = machine_no=request.data.get("machine_no")
            print(1)
            machineNo = Machine.objects.get(id=machine_no)
            print(2)
            serializer = MachineSerializer(machineNo, request.data)
            if serializer.is_valid():
                serializer.save()
                data['status'] = True
                data['message'] = "Data updated successfully"
            else:
                data['status'] = False
                data['message'] = "Invalid data"
        except Exception as e:
            data['status'] = False
            data['message'] = "Failed to update the data"

        return Response(data=data)

    def post(self, request):
        data = {}
        try:
            if Machine.objects.get(machine_no=request.data.get("machine_no")):
                serializer = MachineSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    data['status'] = True
                    data['message'] = "Data saved successfully"
            else:
                data['status'] = False
                data['message'] = "Invalid data"
        except Exception as e:
            data['status'] = False
            data['message'] = "Failed to save the data"

        return Response(data=data)

    def delete(self, request):
        data = {}
        try:
            book = Machine.objects.get(machine_no=request.query_params.get("machine_no"))
            book.delete()
            data['status'] = True
            data['message'] = "Book deleted successfully"
        except Exception as e:
            data['status'] = False
            data['message'] = "Failed to delete book"

        return Response(data=data)


@csrf_exempt
def StatsMachine(request, machine_no=None):
    data = {}
    if machine_no:
        try:
            g = Machine.objects.get(machine_no=machine_no)
            data['machine_status'] = g.machine_status
            data['machine_no'] = g.machine_no
            # data['food'] = ' tinapay'
            return HttpResponse(data)
        except Exception as e:
            pass
    return HttpResponse(f"macnine no.  {machine_no}" )
    # return HttpResponse("<p> asdc wdadw </p>")




@csrf_exempt
def AjaxAPI(request):
    try:
        McNo = request.GET.get('machine_status')
        print("-------------------------", McNo)
        if request.is_ajax():
            g = Machine.objects.get(machine_no="1")
            return JsonResponse({'machine_status':g.machine_status}, status=200)
    except Exception as e:
        pass
    return render(request, 'main/index.html')
    # return HttpResponse(f"macnine no.  {request}" )



@csrf_exempt
def Home(request):
    return render(request, "main/index.html")