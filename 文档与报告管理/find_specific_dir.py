#!/usr/bin/python3
#-*- coding:UTF-8 -*-
import os
import fnmatch
def is_file_match(filename, patters):
    for pattern in patters:
        if fnmatch.fnmatch(filename, pattern):
            return True
    return False
def find_specific_files(root, patters=['*'], exclude_dirs=[]):
    for root, dirnames, filenames in os.walk(root):
        for d in exclude_dirs:
            if d in dirnames:
                dirnames.remove(d)
        for filename in filenames:
            if is_file_match(filename, patters):
                yield os.path.join(root, filename)

            