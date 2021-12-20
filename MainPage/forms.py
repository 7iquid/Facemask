from django import forms
from django.forms import ModelForm

from api.models import McRecordingArea

ProblemFound= [
	('1.','Nose wire funnel'),
	('2.','Material feeder aligner'),
	('3.','Blanking welding'),
	('4.','Other'),
	]

CounterMeasure= [
	('1.','Align nose wire funnel'),
	('2.','Material aligner'),
	('3.','Blanking welding'),
	('4.','Other'),
	]

class DowntimeReport(ModelForm):
	class Meta:
		model = McRecordingArea
		fields = ['root_cause', 'action_taken', 'remarks',]
	