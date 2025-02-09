import os
import shutil
import time
from typing import List
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_valid_path() -> str:
    while True:
        print("\n=================================")
        print("         FILE ORGANIZER")
        print("=================================\n")
        input_path = input("Enter folder path to organize (or 'exit' to quit): ")
        
        if input_path.lower() == 'exit':
            sys.exit()
            
        folderpath = os.path.join(os.environ['USERPROFILE'], input_path)
        
        if os.path.exists(folderpath):
            return folderpath
        print("\nError: Folder not found. Please try again.")
        time.sleep(2)
        clear_screen()

def get_destination_folder() -> str:
    while True:
        new_folder = input("\nEnter name for destination folder on Desktop: ")
        desktop_path = os.path.join(os.environ['USERPROFILE'], "Desktop", new_folder)
        
        if os.path.exists(desktop_path):
            overwrite = input("\nWarning: Folder exists. Continue anyway? (Y/N): ")
            if overwrite.lower() == 'y':
                return desktop_path
        else:
            return desktop_path

def get_file_extensions(folderpath: str) -> List[str]:
    extensions = set()
    for file in os.listdir(folderpath):
        if os.path.isfile(os.path.join(folderpath, file)):
            ext = os.Dpath.splitext(file)[1][1:]
            if ext:
                extensions.add(ext)
    return list(extensions)

def organize_files(folderpath: str, desktop_path: str, extensions: List[str]):
    os.makedirs(desktop_path, exist_ok=True)
    total_files = len([f for f in os.listdir(folderpath) if os.path.isfile(os.path.join(folderpath, f))])
    processed = 0

    print("\nProcessing files...")
    print("=================================")

    for ext in extensions:
        ext_folder = os.path.join(desktop_path, ext)
        os.makedirs(ext_folder, exist_ok=True)
        
        for file in os.listdir(folderpath):
            if file.endswith(f".{ext}"):
                processed += 1
                source = os.path.join(folderpath, file)
                destination = os.path.join(ext_folder, file)
                shutil.move(source, destination)
                print(f"Processing {processed} of {total_files} files [{ext} files]")

def main():
    while True:
        clear_screen()
        folderpath = get_valid_path()
        desktop_path = get_destination_folder()
        
        extensions = get_file_extensions(folderpath)
        organize_files(folderpath, desktop_path, extensions)
        
        print("\n=================================")
        print("Organization complete!")
        print(f"Files moved to: {desktop_path}")
        
        input("\nPress Enter to organize another folder...")

if __name__ == "__main__":
    main()