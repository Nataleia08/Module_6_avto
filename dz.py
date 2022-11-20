from pathlib import Path

p = Path(input("Введіть шлях до папки:"))
if not p.is_dir:
    print("Це не шлях до папки!")
else:
