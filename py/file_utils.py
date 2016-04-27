from __future__ import print_function
import os
import sys
import string

__all__ = ['get_basename', 'get_extension', 'directory_contains']

def get_basename(fname):
    """
    Get file base name: without extension and path
    foo => foo
    include.c => include
    /opt/foo.txt => foo
    foo.bar.h => foo
    /opt//tomcat/webapps/junk.war => junk
    """
    h,t = os.path.split(fname)
    x = string.split(t, '.')
    return x[0]


def get_extension(fname):
    """
    Get extension of file.
    c.txt => txt
    /opt/c.txt => txt
    ~/myname/foo.bar.x => bar.x
    """
    return None


def directory_contains(dirname, fname):
    """
    True if file fname is in directory dirname.
	Cases:
    - directory must not be null
    - directory must be a directory
    - directory does not contain itself
    - null child file is not contained in any parent
    """
    if dirname is None or fname is None:
        return False
    if os.path.exists(dirname) and os.path.isdir(dirname):
        l = os.listdir(dirname)
        if fname in l:
            if os.path.isfile(fname) and not os.path.islink(fname):
                return True
    return False


def test_get_basename(fname):
    print("test_get_basename:", " path:", fname)
    print("result: ", get_basename(fname))


def test_dir_contains(d, f):
    print("test_dir_contains:", " dir:", d, " file: ", f)
    print("result:", directory_contains(d, f))

if __name__ == "__main__":
    test_get_basename("foo")
    test_get_basename("include.c")
    test_get_basename("/opt/foo.txt")
    test_get_basename("foo.bar.h")
    test_get_basename("/opt//tomcat/webapps/junk.war")
    test_dir_contains(".", "curl_no_proxy.py")
    test_dir_contains(".", "_proxy.py")
