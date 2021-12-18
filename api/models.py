from django.db import models

# Create your models here.

class Machine(models.Model):
	date = models.DateTimeField(auto_now=True)
	machine_no = models.IntegerField(null=False, primary_key=True)
	machine_status = models.BooleanField(null=False)

	def __str__(self):
		return self.machine_no

class McRecordingArea(models.Model):
	root_cause = models.CharField(default='Root Cause',max_length=300)
	action_taken = models.CharField(default='Action Taken',max_length=300)
	remarks = models.CharField(default='Remarks',max_length=300)
	total_down_time_hour = models.IntegerField()
	total_down_time_minute = models.IntegerField()
	machine = models.ForeignKey(Machine, on_delete=models.CASCADE)


	def __str__(self):
		return self.action_taken

	class Meta:
		ordering = ['action_taken']
