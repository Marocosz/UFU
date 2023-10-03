#!/usr/bin/python3

# https://docs.python.org/3/library/os.html
import os
import sys


def dirsize(path):
    sizesum = 0
    if os.access(path, os.R_OK):
        for obj in os.scandir(path):
            if obj.is_file():
                sizesum += obj.stat().st_size
            if obj.is_dir(follow_symlinks=False):
                sizesum += dirsize(obj.path)
    return sizesum


if len(sys.argv) > 1:
    dirname = sys.argv[1]
    print('%.2f Gigabytes' % (dirsize(dirname) / 1024 ** 3))
