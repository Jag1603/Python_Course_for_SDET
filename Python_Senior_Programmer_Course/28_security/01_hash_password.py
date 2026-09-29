import hashlib
password = "demo-password"
digest = hashlib.sha256(password.encode()).hexdigest()
print(digest)