from datetime import datetime
value = datetime.strptime("2026-09-29 10:30", "%Y-%m-%d %H:%M")
print(value.strftime("%d/%m/%Y"))