from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import Machine
from .serializers import MachineSerializer


from pyfiglet import Figlet
f = Figlet(font='slant')
#/api/no

class MachineStatus(APIView):
  
    @csrf_exempt
    def get(self, request):
        data = {}
 
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
        try:
            machineNo = Machine.objects.get(machine_no=request.data.get("machine_no"))
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
    # data = {}
    # if machine_no:
    #     # g = Machine.objects.get(machine_no=machine_no)
    #     # data['machine_status'] = g.machine_status
    #     data['name'] = "pogi"
    #     data['food'] = ' tinapay'
    #     return Response(machine_no)
    return HttpResponse(f"macnine no.  {machine_no}" )
    # return HttpResponse("<p> asdc wdadw </p>")

@csrf_exempt
def Home(request):
    return render(request, "main/index.html")