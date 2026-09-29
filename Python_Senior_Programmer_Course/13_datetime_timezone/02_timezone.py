from datetime import datetime, timezone
from zoneinfo import ZoneInfo
now = datetime.now(timezone.utc)
print(now.astimezone(ZoneInfo("Asia/Kolkata")))