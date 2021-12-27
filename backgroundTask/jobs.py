from django.conf import settings
import requests
import json
import random


from datetime import datetime
from api.models import McDailyRecordingArea

def schedule_api():
	dateChecker()
	statusran = str(datetime.now().date())
	print(f'today date added: {statusran}')


def dateChecker():
	dateNow = str(datetime.now().date())
	try:
		dbdateNow = McDailyRecordingArea.objects.get(dailydate=dateNow)
		
	except:
		print('no data found  saving current date')
		dat = McDailyRecordingArea(
			dailydate = dateNow,
			)
		dat.save()

