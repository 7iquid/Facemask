import requests

url ='http://192.168.1.44:8000/api/'

data={
	"machine_no": 1,
	'machine_status': True ,
}

rep = requests.put(url, data)
print(rep.text)