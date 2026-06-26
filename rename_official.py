import json
import os
import re
from pathlib import Path

EXPORT_DIR = Path.home() / "leetcode-export"

# Load official LeetCode problem list
with open(EXPORT_DIR / "problems.json", "r") as f:
    data = json.load(f)

mapping = {}

for p in data["stat_status_pairs"]:
    slug = p["stat"]["question__title_slug"]
    qid = p["stat"].get("frontend_question_id") or p["stat"]["question_id"]
    mapping[slug] = int(qid)

renamed = 0
skipped = 0

for item in os.listdir(EXPORT_DIR):
    full = EXPORT_DIR / item

    if not full.is_dir():
        continue

    m = re.match(r"^\d+-(.+)$", item)
    if not m:
        continue

    slug = m.group(1)

    if slug not in mapping:
        print(f"Skipping: {item}")
        skipped += 1
        continue

    new_name = f"{mapping[slug]:04d}-{slug}"
    target = EXPORT_DIR / new_name

    if target.exists():
        print(f"Already exists: {new_name}")
        skipped += 1
        continue

    print(f"{item}  -->  {new_name}")
    full.rename(target)
    renamed += 1

print()
print(f"Renamed: {renamed}")
print(f"Skipped: {skipped}")
