import os
import shutil

def organize_files(folder_path):
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".txt"],
        "CSV_Files": [".csv"],
        "Others": []
    }

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            moved = False
            for folder, extensions in file_types.items():
                if any(filename.lower().endswith(ext) for ext in extensions):
                    folder_dir = os.path.join(folder_path, folder)
                    os.makedirs(folder_dir, exist_ok=True)
                    shutil.move(file_path, os.path.join(folder_dir, filename))
                    moved = True
                    break

            if not moved:
                folder_dir = os.path.join(folder_path, "Others")
                os.makedirs(folder_dir, exist_ok=True)
                shutil.move(file_path, os.path.join(folder_dir, filename))

if __name__ == "__main__":
    path = input("Enter the folder path to organize: ")
    organize_files(path)
    print("✅ Files organized successfully!")
