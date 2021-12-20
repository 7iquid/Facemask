from django.db import models

# Create your models here.

class Machine(models.Model):
	date = models.DateTimeField(auto_now=True) #auto_now update auto_now_add created
	machine_no = models.IntegerField(null=False, primary_key=True)
	machine_status = models.BooleanField(null=False)

	def __str__(self):
		return self.machine_no

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

	root_cause = models.CharField(default='Root Cause',max_length=300,choices=ProblemFound)
	action_taken = models.CharField(default='Action Taken',max_length=300,choices=CounterMeasure)
	remarks = models.CharField(null=True, default='Remarks',max_length=300)
	total_down_time  = models.FloatField(null=True, default=None)
	machine = models.ForeignKey(Machine, on_delete=models.CASCADE)

	def __str__(self):
		return self.action_taken

	class Meta:
		ordering = ['machine','total_down_time','action_taken','root_cause']
