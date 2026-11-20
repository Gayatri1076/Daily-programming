import os
import shutil

folder = input("Enter folder path: ")

categories = {
    "Images": [".jpg", ".png", ".jpeg"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Music": [".mp3", ".wav"]
}

if os.path.isdir(folder):
    for file in os.listdir(folder):
        path = os.path.join(folder, file)

        if os.path.isfile(path):
            extension = os.path.splitext(file)[1].lower()

            for category, extensions in categories.items():
                if extension in extensions:
                    target = os.path.join(folder, category)
                    os.makedirs(target, exist_ok=True)

                    shutil.move(path, os.path.join(target, file))
                    print(file, "->", category)
                    break

    print("File organization completed!")
else:
    print("Invalid folder path!")