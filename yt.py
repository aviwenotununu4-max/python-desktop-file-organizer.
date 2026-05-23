import os
import shutil
from pathlib import Path


def clean_folder():
    # 1. Define the directory you want to clean
    # You can change this to your Desktop or Downloads path
    target_dir = input("📁 Enter the full folder path to organize: ").strip()

    path = Path(target_dir)
    if not path.exists():
        print("❌ Error: That folder path does not exist!")
        return

    # 2. Define your sorting rules
    FILE_CATEGORIES = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
        "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
        "Videos": [".mp4", ".mkv", ".mov", ".avi"],
        "Audio": [".mp3", ".wav", ".flac"],
        "Zip_Files": [".zip", ".rar", ".7z", ".tar.gz"]
    }

    print("⏳ Sorting files... Please wait...")
    moved_count = 0

    # 3. Loop through files and move them
    for item in path.iterdir():
        if item.is_file():
            file_extension = item.suffix.lower()

            for folder_name, extensions in FILE_CATEGORIES.items():
                if file_extension in extensions:
                    # Create the category folder if it doesn't exist
                    destination_folder = path / folder_name
                    destination_folder.mkdir(exist_ok=True)

                    # Move the file safely
                    shutil.move(str(item), str(destination_folder / item.name))
                    print(f"📁 Moved: {item.name} -> {folder_name}/")
                    moved_count += 1
                    break

    print(f"✅ Finished! Successfully organized {moved_count} files.")


if __name__ == "__main__":
    clean_folder()
