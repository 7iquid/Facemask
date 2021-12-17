from django.conf import settings
import requests
import json
import random


postcodes = [
	True,
	False, 
	False,
	True
]

def schedule_api():

	statusran = postcodes[random.randint(0, 3)]

	# full_url = f"https://api.postcodes.io/postcodes/{postcode}"
			
	# r = requests.get(full_url)
	# if r.status_code == 200:

	# 	result = r.json()["result"]

	# 	lat = result["latitude"]
	# 	lng = result["longitude"]

	print(f'Latitude: {statusran}')

		#77779

