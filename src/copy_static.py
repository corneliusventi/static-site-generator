import os
import shutil


def copy_static(to_path, from_path):
    if not os.path.exists(to_path):
        os.mkdir(to_path)
    items = os.listdir(from_path)
    for item in items:
        new_to_path = os.path.join(to_path, item)
        new_from_path = os.path.join(from_path, item)
        if os.path.isfile(new_from_path):
            shutil.copy(new_from_path, new_to_path)
        else:
            copy_static(new_to_path, new_from_path)
