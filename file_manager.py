import os
import shutil

path = input("Enter your path: ")

files = os.listdir(path)

for i in files:
    filename, extension = os.path.splitext(i)
    extension_1 = extension[1:]
    folder_path = os.path.join(path, extension_1)
    if os.path.exists(folder_path):
        shutil.move(os.path.join(path, i), os.path.join(folder_path, i))
    else:
        os.makedirs(folder_path)
        shutil.move(os.path.join(path, i), os.path.join(folder_path, i))
