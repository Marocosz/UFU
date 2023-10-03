#!/usr/bin/python3

# https://docs.python.org/3/library/os.html
import os
import sys


def lookfor(path, ext):
    if os.access(path, os.R_OK):
        for obj in os.scandir(path):
            if obj.is_file():
                if os.path.splitext(obj.name)[1].lower() == '.' + ext:
                    print(obj.path)
            if obj.is_dir(follow_symlinks=False):
                lookfor(obj.path, ext)


if len(sys.argv) > 1:
    ext = sys.argv[1]
    lookfor('.', ext.lower())

