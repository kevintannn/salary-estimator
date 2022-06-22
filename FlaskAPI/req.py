import requests
from dummy import data_in

url = "http://127.0.0.1:5000/predict"
header = {"Content-Type": "application/json"}
data = {"input": data_in}

r = requests.get(url, headers=header, json=data)

print(r.json())