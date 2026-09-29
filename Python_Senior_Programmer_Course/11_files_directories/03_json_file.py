import json
from pathlib import Path
data = {"name":"Ada","skills":["Python","Testing"]}
Path("user.json").write_text(json.dumps(data, indent=2), encoding="utf-8")
print(json.loads(Path("user.json").read_text(encoding="utf-8")))