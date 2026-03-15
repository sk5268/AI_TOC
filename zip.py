import zipfile
import os
from pathlib import Path

def create_zip(manifest_source, zip_name):
    """
    Create a zip file for a specific browser extension.
    """
    common_files = ['code.css', 'code.js']
    icons_dir = 'icons'
    
    print(f"Creating {zip_name}...")
    
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Add manifest (renamed to manifest.json inside the zip)
        manifest_path = Path(manifest_source)
        if manifest_path.exists():
            zipf.write(manifest_path, 'manifest.json')
            print(f"  Added {manifest_source} as manifest.json")
        else:
            print(f"  Warning: {manifest_source} not found")

        # Add common files
        for file_name in common_files:
            file_path = Path(file_name)
            if file_path.exists():
                zipf.write(file_path, file_name)
                print(f"  Added {file_name}")
            else:
                print(f"  Warning: {file_name} not found")
        
        # Add icons directory
        icons_path = Path(icons_dir)
        if icons_path.exists() and icons_path.is_dir():
            for file in icons_path.rglob('*'):
                if file.is_file():
                    zipf.write(file, file)
                    print(f"  Added {file}")
        else:
            print("  Warning: icons directory not found")
    
    print(f"Finished creating {zip_name}\n")

def main():
    # Create zips for both Chrome and Firefox
    create_zip('chrome_manifest.json', 'chrome.zip')
    create_zip('firefox_manifest.json', 'firefox.zip')
    print("All zips created successfully.")

if __name__ == "__main__":
    main()
