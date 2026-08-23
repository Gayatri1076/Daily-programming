import os
import shutil

folder = input("Enter folder path: ")

if not os.path.exists(folder):
    print("Folder not found!")
else:
    for file in os.listdir(folder):

        file_path = os.path.join(folder, file)

        if os.path.isfile(file_path):

            extension = os.path.splitext(file)[1].lower()

            if extension:
                folder_name = extension[1:].upper() + "_Files"
            else:
                folder_name = "Other_Files"

            new_folder = os.path.join(folder, folder_name)

            if not os.path.exists(new_folder):
                os.makedirs(new_folder)

            shutil.move(
                file_path,
                os.path.join(new_folder, file)
            )

    print("Files organized successfully!")