
'''
readme

variable (date.time - date.time)

subtract date return total hours type float
'''
from datetime import datetime


def DateSubtract(oldtime, newtime=datetime.now()):
	# timebefore = datetime.timestamp(oldtime)
	# timeafter =  datetime.timestamp(newtime)
	try:
		if newtime > oldtime:
			dt_object1 = (newtime - oldtime)
		
		else:
			dt_object1 = (oldtime - newtime)
		print(type(dt_object1),dt_object1,"===1")


		seconds = dt_object1.total_seconds()
		print(type(seconds),seconds,"===4")

		h = seconds/3600
		print(h,"===5")
		h1 = round(h,2)
		print(h1,"===6")
		return h1
	except:
		print('fail date and time')

# print(datetime.now().date())
		