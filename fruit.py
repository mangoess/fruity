import requests
import time
import json

def fruit(fruit):
  x = requests.get('https://fruityvice.com/api/fruit/{}'.format(fruit)
  print("Status Code", x.status_code)
  print(x)
  
  # GETTING INFORMATION OFF : https://fruityvice.com/api/fruit/(fruit)
  # REQUEST TYPE : GET
  # REQUEST FOR ALL FRUITS : https://fruityvice.com/api/fruit/all
  
  #THIS IS A TEST BRANCH, NOT INTENDED FOR USE YET.