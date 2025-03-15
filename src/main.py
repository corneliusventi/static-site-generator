import os
import shutil
from copy_static import copy_static


public_path="./public"
static_path="./static"


def main():
    if os.path.exists(public_path):
        shutil.rmtree(public_path)
    copy_static()


if __name__ == "__main__":
    main()
