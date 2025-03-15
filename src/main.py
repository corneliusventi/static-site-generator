import sys
import os
import shutil
from copy_static import copy_static
from generate_page import generate_pages_recursive


public_path="./docs"
static_path="./static"
content_path="./content"
template_path="./template.html"


def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    if os.path.exists(public_path):
        shutil.rmtree(public_path)
    copy_static(public_path, static_path)
    generate_pages_recursive(content_path, template_path, public_path, basepath)


if __name__ == "__main__":
    main()
