import re
m = re.match(r"(\w+)-(\d+)", "BUG-123")
print(m.groups())