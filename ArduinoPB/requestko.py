import requests

url ='http://127.0.0.1:8000/api/'

data={
	"machine_no": 1,
	'machine_status': True ,
}

rep = requests.put(url, data)
print(rep.text)