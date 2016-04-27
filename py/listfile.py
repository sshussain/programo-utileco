#!/usr/bin/env python
from __future__ import print_function
import os
import sys

def is_file_of_type(fname, ftype=[]):
    if len(ftype) == 0:
        return True
    _,extension = os.path.splitext(fname)
    extension = extension.replace(".", "")
    if len(extension) == 0:
        return False
    if extension in ftype:
        return True
    return False


def showdir(d, ftype=[]):
    '''
    Get list of files in specified directory. A file should not be a symbolic link.
    '''
    l = []
    if os.path.exists(d):
        for fname in os.listdir(d):
            if os.path.isfile(fname) and not os.path.islink(fname):
                if is_file_of_type(fname, ftype):
                    l.append(fname)
    return l

def print_fname(flist):
    for fname in sorted(flist, key=str.lower):
        print(fname)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Not enough arguments")
        sys.exit(-1)

    srcdir = '.'

    args = sys.argv[1:]
    if len(sys.argv) >= 1 :
        srcdir = args[0]
        types = args[1:]
    print_fname(showdir(srcdir, types))
