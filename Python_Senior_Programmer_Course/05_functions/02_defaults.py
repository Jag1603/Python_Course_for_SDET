def connect(host="localhost", port=5432):
    return f"{host}:{port}"
print(connect())
print(connect(port=3306))