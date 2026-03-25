import os
from pathlib import Path

def setup_base_folders(base_path="D:\\food"):
    """Creates the base raw and final folders."""
    folders = ["raw", "final"]
    
    for folder in folders:
        path = Path(base_path) / folder
        path.mkdir(parents=True, exist_ok=True)
        print(f"Ensured {path} exists.")

if __name__ == "__main__":
    setup_base_folders()
