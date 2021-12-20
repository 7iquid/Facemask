
'''
readme

variable (date.time - date.time)

subtract date return total hours type float
'''
from datetime import datetime


def DateSubtract(oldtime, newtime=datetime.now()):
	timebefore = datetime.timestamp(oldtime)
	timeafter =  datetime.timestamp(newtime)
	try:
		dt_object1 = (timeafter - timebefore)
		print(dt_object1,"===1")

		# timestamp = 1545730073
		dt_object2 = datetime.fromtimestamp(dt_object1)
		print(dt_object2,"===2")

		a_timedelta = dt_object2 - datetime(1970, 1, 1)
		print(a_timedelta,"===3")

		seconds = a_timedelta.total_seconds()
		print(seconds,"===4")

		h = seconds/3600
		print(h,"===5")
		h1 = round(h,2)
		print(h1,"===6")
		return h1
	except:
		print('fail date and time')
		