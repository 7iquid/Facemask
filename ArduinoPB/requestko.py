import requests

pc ='http://127.0.0.1:8000/api/'
pi = 'http://192.168.1.54:8000/api/'
url= pc

data={
	'apikey':'papa pogi',
	"machine_no": 4,
	# 'machine_status': True
	
	}

rep = requests.post(url, data)
print(rep.text)