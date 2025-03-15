import os
import shutil
from copy_static import copy_static
from generate_page import generate_page


public_path="./public"
static_path="./static"
content_path="./content"
template_path="./template.html"


def main():
    if os.path.exists(public_path):
        shutil.rmtree(public_path)
    copy_static(public_path, static_path)
    generate_page(
        os.path.join(content_path, "index.md"),
        template_path,
        os.path.join(public_path, "index.html"),
    )


if __name__ == "__main__":
    main()
