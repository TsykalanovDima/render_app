import requests
import json

url = 'https://render-app-teot.onrender.com/greet'
data = {'name': 'Vitala'}
headers = {'Content-Type': 'application/json'}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.json())
