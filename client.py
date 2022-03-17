import requests

res = requests.get("http://localhost:5000/weather")


print(res.status_code)

data = res.json()

print(data)