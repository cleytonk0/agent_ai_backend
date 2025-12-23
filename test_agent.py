import requests

url = "http://127.0.0.1:8000/agent"
data = {"user_input": "Olá, como você está?"}

response = requests.post(url, json=data)
print("Status Code:", response.status_code)
print("Response:", response.json())