import requests
import time
import json

def getfruitname(fruit):
  x = requests.get('https://fruityvice.com/api/fruit/{}'.format(fruit) )
  print("Status Code", x.status_code)
  fruit = x.text
  
  
def getfruitelement(element):
  y = requests.get('https://fruityvice.com/api/fruit/{}'.format(fruit) )
  data = (y.text)
  json_object = json.loads(y.text)
  print(json_object["{}"].format(element) )
json_object["genus"])

  # GETTING INFORMATION OFF : https://fruityvice.com/api/fruit/(fruit)
  # REQUEST TYPE : GET
  # REQUEST FOR ALL FRUITS : https://fruityvice.com/api/fruit/all
  
  #THIS IS A TEST BRANCH, NOT INTENDED FOR USE YET.

  
