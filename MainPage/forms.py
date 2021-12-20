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

class DowntimeReport(forms.Form):
	class Meta:
		model = McRecordingArea
		fields = ['root_cause', 'action_taken', 'remarks', 'total_down_time']
	# root_cause = forms.CharField(label='Please Select',widget=forms.Select(choices=INTEGER_CHOICES))
	# root_cause = forms.ChoiceField(choices=ProblemFound)
	# action_taken = forms.ChoiceField(choices=CounterMeasure)
	# remarks = forms.CharField(widget=forms.TextInput(attrs={'size': '40'}))
	# username=forms.CharField(max_length=30, widget=forms.TextInput(attrs={'size':'80'}))
    # first_name= forms.CharField(max_length=100)
    # last_name= forms.CharField(max_length=100)
    # email= forms.EmailField()
    # age= forms.IntegerField()
    # todays_date= forms.IntegerField(label="What is today's date?", widget=forms.Select(choices=INTEGER_CHOICES))

# class DowntimeReport(ModelForm):
# 	class Meta:
# 		model = McRecordingArea
# 		fields = ['root_cause', 'action_taken']
