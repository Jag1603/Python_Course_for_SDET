from pathlib import Path
root = Path(".")
for path in root.glob("*.py"):
    print(path)