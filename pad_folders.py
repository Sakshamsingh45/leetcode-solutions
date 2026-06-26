import os
import re
from pathlib import Path

BASE = Path.home() / "leetcode-export"

for folder in BASE.iterdir():
    if not folder.is_dir():
        continue

    match = re.match(r"^(\d+)-(.*)$", folder.name)
    if not match:
        continue

    number = int(match.group(1))
    slug = match.group(2)

    new_name = f"{number:04d}-{slug}"
    new_path = BASE / new_name

    # Skip if already renamed
    if folder.name == new_name:
        continue

    # Skip if destination already exists
    if new_path.exists():
        print(f"Skipping (already exists): {new_name}")
        continue

    folder.rename(new_path)
    print(f"{folder.name}  -->  {new_name}")

print("\nDone!")
