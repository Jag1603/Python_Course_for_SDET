import requests
response = requests.get("https://httpbin.org/get", timeout=10)
print(response.status_code)
print(response.json()["url"])