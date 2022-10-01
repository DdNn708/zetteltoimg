import os
import shutil

"""
Use Case
1. Manually copy b_box files to tmp directory
2. Perform the function 'edit_image'
3. Perform the function 'copytree'
"""

src = "/Users/dnv/Downloads/img_from_html"
dst = "/Users/dnv/Library/Mobile Documents/iCloud~md~obsidian/Documents/Z_copy/b_box_copy"


def copytree(src: str, dst: str, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)


if __name__ == '__main__':
    copytree(src=src, dst=dst)
