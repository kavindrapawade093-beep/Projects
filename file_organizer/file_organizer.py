# ---------------------------------
# File Organizer Project
# ---------------------------------

import os
import shutil

print("===== FILE ORGANIZER =====")

# Folder Path
path = input("Enter Folder Path: ")

# Get Files
files = os.listdir(path)

for file in files:

    # File Path
    file_path = os.path.join(path, file)

    # Skip Folders
    if os.path.isdir(file_path):
        continue

    # File Extension
    extension = file.split(".")[-1]

    # Create Folder
    folder_name = extension.upper() + "_Files"

    folder_path = os.path.join(path, folder_name)

    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    # Move File
    shutil.move(file_path, os.path.join(folder_path, file))

print("\nFiles Organized Successfully!")
