import csv
import shutil
import argparse
from pathlib import Path

def process_brand(base_dir, brand_name, csv_path):
    base_path = Path(base_dir)
    final_dir = base_path / "final"
    brand_dir = base_path / brand_name
    
    if not final_dir.exists():
        print(f"Error: Final directory '{final_dir}' does not exist.")
        return
        
    if not Path(csv_path).exists():
        print(f"Error: CSV file '{csv_path}' does not exist.")
        return

    # Read CSV
    # Expected columns: System Category, Brand Category, System Item, Brand Item
    with open(csv_path, mode='r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        
        # Verify columns
        expected_cols = ["System Category", "Brand Category", "System Item", "Brand Item"]
        for col in expected_cols:
            if col not in reader.fieldnames:
                print(f"Error: CSV must contain column '{col}'. Found columns: {reader.fieldnames}")
                return
                
        for row in reader:
            sys_cat = row["System Category"].strip()
            brand_cat = row["Brand Category"].strip()
            sys_item = row["System Item"].strip()
            brand_item = row["Brand Item"].strip()
            
            if not sys_item or not brand_item:
                continue
                
            # Find image in final folder
            # Look for exact match by name without extension, or assume .jpg, .png etc.
            found_img = None
            for ext in [".jpg", ".png", ".webp", ".jpeg", ".JPG", ".PNG"]:
                test_path = final_dir / f"{sys_item}{ext}"
                if test_path.exists():
                    found_img = test_path
                    break
            
            if not found_img:
                print(f"Warning: Could not find image for '{sys_item}' in {final_dir}")
                continue
                
            # Setup destination paths
            dest_raw_dir = brand_dir / "brand-raw" / brand_cat / brand_item
            dest_ready_dir = brand_dir / "ready" / brand_cat / brand_item
            
            dest_raw_dir.mkdir(parents=True, exist_ok=True)
            dest_ready_dir.mkdir(parents=True, exist_ok=True)
            
            # Target file path
            dest_file = dest_raw_dir / f"{brand_item}{found_img.suffix}"
            
            # Copy image
            try:
                shutil.copy2(found_img, dest_file)
                print(f"Copied {found_img.name} -> {dest_file}")
            except Exception as e:
                print(f"Failed to copy {found_img.name}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process brand images from final folder.")
    parser.add_argument("brand_name", help="Name of the brand folder to create (e.g., 'the wok')")
    parser.add_argument("csv_file", help="Path to the mapping CSV file")
    parser.add_argument("--base_dir", default="D:\\food", help="Base food directory")
    
    args = parser.parse_args()
    process_brand(args.base_dir, args.brand_name, args.csv_file)
