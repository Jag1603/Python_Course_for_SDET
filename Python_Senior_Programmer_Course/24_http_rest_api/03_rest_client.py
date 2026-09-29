import requests
class ApiClient:
    def __init__(self, base_url): self.base_url = base_url.rstrip("/")
    def get(self, path): return requests.get(self.base_url + path, timeout=10)
client = ApiClient("https://httpbin.org")
print(client.get("/get").status_code)