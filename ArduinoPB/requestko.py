import requests

pc ='http://127.0.0.1:8000/api/'
pi = 'http://192.168.1.150:8000/api/'
url= pi

data={
	'apikey':'machine_status',
	"machine_no": 1,
	'machine_status': False ,
	
	}

rep = requests.put(url, data)
print(rep.text)