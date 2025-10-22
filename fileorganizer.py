# file_organizer.py
import os, shutil
ext_map = {'images': ['.png', '.jpg'], 'docs': ['.pdf', '.txt'], 'videos': ['.mp4']}
path = "C:/Users/You/Downloads"

for file in os.listdir(path):
    full = os.path.join(path, file)
    if os.path.isfile(full):
        for folder, exts in ext_map.items():
            if any(file.endswith(ext) for ext in exts):
                shutil.move(full, os.path.join(path, folder, file))
                break
