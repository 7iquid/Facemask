from django.db import models

# Create your models here.

class Machine(models.Model):
	date = models.DateTimeField(auto_now_add=True)
	machine_no = models.IntegerField(null=False, default=1)
	machine_status = models.BooleanField(null=False, default=False)
	status_update = models.DateTimeField(default=now, blank=True)

	def __str__(self):
		return self.machine_no