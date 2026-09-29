from pathlib import Path
p = Path("sample.txt")
p.write_text("Python\nAutomation\n", encoding="utf-8")
print(p.read_text(encoding="utf-8"))