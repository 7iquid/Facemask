from django.db import models

# Create your models here.

class Machine(models.Model):
	date = models.DateTimeField(auto_now=True)
	machine_no = models.IntegerField(null=False)
	machine_status = models.BooleanField(null=False)

	def __str__(self):
		return self.machine_no

class McRecordingArea(models.Model):
	action_taken = models.CharField(max_length=300)
	total_down_time_hour = models.IntegerField()
	total_down_time_minute = models.IntegerField()
	machine = models.ForeignKey(Machine, on_delete=models.CASCADE)


	def __str__(self):
		return self.action_taken

	class Meta:
		ordering = ['action_taken']
