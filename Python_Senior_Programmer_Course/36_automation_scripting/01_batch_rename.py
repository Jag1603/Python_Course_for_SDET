from pathlib import Path
root=Path("demo_files")
root.mkdir(exist_ok=True)
for i in range(3): (root/f"file_{i}.txt").write_text("demo")
for p in root.glob("file_*.txt"):
    print("Would rename:", p)