import requests
import json

url = 'http://127.0.0.1:81/greet'
data = {'name': 'Vitala'}
headers = {'Content-Type': 'application/json'}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.json())
