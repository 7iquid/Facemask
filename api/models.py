from django.db import models
from datetime import datetime
# Create your models here.

class Machine(models.Model):
	date = models.DateTimeField(auto_now=True) #auto_now update auto_now_add created
	machine_no = models.IntegerField(null=False, primary_key=True)
	machine_status = models.BooleanField(null=False)

	def __str__(self):
		return self.machine_no



class McDailyRecordingArea(models.Model):
	dailydate = models.DateTimeField(primary_key=True,null=False, unique=True)
	# def __str__(self):
		# return  "something"

		# >>> print(data2)
		# <QuerySet [<McDailyRecordingArea: something>]>




class McRecordingArea(models.Model):
	ProblemFound= [
		('Nose','Nose wire funnel'),
		('feeder','Material feeder aligner'),
		('welding','Blanking welding'),
		('Other','Other'),
		]

	CounterMeasure= [
		('1.','Align nose wire funnel'),
		('aligner','Material aligner'),
		('Blanking','Blanking welding'),
		('Other','Other'),
		]

	root_cause 		= models.CharField(default='Root Cause',max_length=300,choices=ProblemFound)
	action_taken 	= models.CharField(default='Action Taken',max_length=300,choices=CounterMeasure)
	remarks 		= models.CharField(null=True, default='Remarks',max_length=300)
	total_down_time  = models.FloatField(null=False, default=None, )
	by				= models.CharField(default='Name', null=False, max_length=20)
	machine 		= models.ForeignKey(Machine, on_delete=models.CASCADE)
	dalydate 		= models.ForeignKey(McDailyRecordingArea, on_delete=models.CASCADE, null=False)

	# def __str__(self):
	# 	return self.action_taken

	# class Meta:
	# 	ordering = ['machine','total_down_time','action_taken','root_cause']

	# >>> data3 = McRecordingArea.objects.all()
	# >>> print(data3)
	# <QuerySet [<McRecordingArea: Blanking>, <McRecordingArea: Blanking>, <McRecordingArea: Blanking>, <McRecordingArea: aligner>, <McRecordingArea: 1.>, <McRecordingArea: 1.>, <McRecordingArea: 1.>, <McRecordingArea: aligner>, <McRecordingArea: aligner>]>




class JoForms(models.Model):
	MotheJO					= models.CharField(primary_key=True,null=False, unique=True,max_length=300)
	RefPoNo					= models.CharField(null=True,max_length=300)
	RefQtnNo				= models.CharField(null=True,max_length=300)
	RefDrawingNo			= models.CharField(null=True,max_length=300)
	Customer 				= models.CharField(null=True,max_length=300)
	PoDate 					= models.CharField(null=True,max_length=300)
	DateIssued 				= models.CharField(null=True,max_length=300)
	CompletionDateInPo		= models.CharField(null=True,max_length=300)
	DeliveryDateToCustomer	= models.CharField(null=True,max_length=300)
	SalesInCharge			= models.CharField(null=True,max_length=300)