import requests
import json

def fruitz(fruit):
  x = requests.get('https://fruityvice.com/api/fruit/{}'.format(fruit))
  print("Status Code", x.status_code)
  print(x.text)
  code = x.status_code

#x = requests.get('https://fruityvice.com/api/fruit/(fruit)')
#print("\n", x.text)

#load the data into an element
#data = (x.text)

#json_object = json.loads(x.text)

#print(json_object["genus"])

  # GETTING INFORMATION OFF : https://fruityvice.com/api/fruit/(fruit)
  # REQUEST TYPE : GET
  # REQUEST FOR ALL FRUITS : https://fruityvice.com/api/fruit/all
  
  #THIS IS A TEST BRANCH, NOT INTENDED FOR USE YET.
