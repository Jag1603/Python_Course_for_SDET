import re
text = "Contact qa@example.com"
match = re.search(r"[\w.-]+@[\w.-]+", text)
print(match.group() if match else "No email")