import json
payload = '{"id": 101, "status": "PASS"}'
data = json.loads(payload)
print(data)
print(json.dumps(data, indent=2))