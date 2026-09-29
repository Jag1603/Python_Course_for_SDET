from pathlib import Path
root=Path(".")
files=list(root.rglob("*.py"))
print("Python files:", len(files))
for p in files[:10]: print(p)