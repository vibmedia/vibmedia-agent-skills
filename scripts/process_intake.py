import csv
import shutil
import argparse
import re
from pathlib import Path
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def process_intake(base_dir, csv_path):
    base_path = Path(base_dir)
    intake_dir = base_path / "intake"
    raw_dir = base_path / "raw"
    csv_file_path = Path(csv_path)
    
    if not intake_dir.exists():
        print(f"Error: Intake directory {intake_dir} does not exist.")
        return
        
    raw_dir.mkdir(parents=True, exist_ok=True)
    
    mappings = []
    with open(csv_file_path, mode='r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            sys_item = row["System Item"].strip()
            brand_item = row["Brand Item"].strip()
            if sys_item:
                mappings.append({
                    "sys_item": sys_item,
                    "brand_item": brand_item
                })

    fluff = {"pieces", "piece", "pcs", "gravy", "dry", "specials", "classic", "style", "mixed"}
    moved_count = 0
    auto_added_count = 0
    new_csv_rows = []
    
    for file_path in list(intake_dir.iterdir()):
        if not file_path.is_file():
            continue
            
        file_name_stem = file_path.stem.lower()
        if file_name_stem.startswith("img"):
            continue
            
        file_name_clean = file_name_stem.replace("paper", "pepper").replace("momos", "momo")
        file_words = set(re.findall(r'[a-z0-9]+', file_name_clean)) - fluff
        
        if not file_words:
            continue
            
        file_name_joined = " ".join(sorted(file_words))
        
        best_match = None
        best_score = 0.0
        
        for m in mappings:
            sys_words = set(re.findall(r'[a-z0-9]+', m['sys_item'].lower())) - fluff
            sys_joined = " ".join(sorted(sys_words))
            brand_words = set(re.findall(r'[a-z0-9]+', m['brand_item'].lower())) - fluff
            brand_joined = " ".join(sorted(brand_words))
            
            score_sys = similar(sys_joined, file_name_joined)
            score_brand = similar(brand_joined, file_name_joined)
            
            if sys_words and sys_words.issubset(file_words):
                score_sys = 1.0
            if brand_words and brand_words.issubset(file_words):
                score_brand = 1.0
                
            max_score = max(score_sys, score_brand)
            if max_score > best_score:
                best_score = max_score
                best_match = m
                
        if best_match and best_score >= 0.70:
            sys_item_target = best_match['sys_item']
            dest_file = raw_dir / f"{sys_item_target}{file_path.suffix}"
            
            counter = 1
            while dest_file.exists():
                dest_file = raw_dir / f"{sys_item_target}_{counter}{file_path.suffix}"
                counter += 1
            
            try:
                shutil.move(str(file_path), str(dest_file))
                print(f"[{best_score:.2f}] Matched '{file_path.name}' -> '{dest_file.name}'")
                moved_count += 1
            except Exception as e:
                print(f"Error moving {file_path.name}: {e}")
                
        elif re.match(r'^[A-Za-z\s]+$', file_path.stem):
            # Auto-generation fallback logic for unmapped clear item names
            sys_item_target = file_path.stem.title()
            dest_file = raw_dir / f"{sys_item_target}{file_path.suffix}"
            
            counter = 1
            while dest_file.exists():
                dest_file = raw_dir / f"{sys_item_target}_{counter}{file_path.suffix}"
                counter += 1
                
            try:
                shutil.move(str(file_path), str(dest_file))
                print(f"[AUTO-GEN] Unmapped descriptive item '{file_path.name}' -> '{dest_file.name}'")
                new_csv_rows.append(["Uncategorized", "", sys_item_target, ""])
                auto_added_count += 1
                moved_count += 1
            except Exception as e:
                print(f"Error auto-moving {file_path.name}: {e}")
                
    if new_csv_rows:
        with open(csv_file_path, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            for row in new_csv_rows:
                writer.writerow(row)
        print(f"Added {auto_added_count} new entries to {csv_file_path.name}")
        
    print(f"Done processing. Moved a total of {moved_count} files to raw folder.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_file")
    parser.add_argument("--base_dir", default="D:\\food")
    args = parser.parse_args()
    process_intake(args.base_dir, args.csv_file)
