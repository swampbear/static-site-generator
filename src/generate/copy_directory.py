import os
import shutil


def copy_directory(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)

    os.mkdir(destination)
    dir = os.listdir(source)
    for sub in dir:
        s_path = f"{source}/{sub}"
        if os.path.isfile(s_path):
            shutil.copy(s_path, destination)
            print(f"Copied: {s_path}")
        else:
            d_path = f"{destination}/{sub}"
            copy_directory(s_path, d_path)
