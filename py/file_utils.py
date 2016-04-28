from __future__ import print_function
import os, sys
import string
import tempfile
from shutil import copy2, copytree, ignore_patterns, move


__all__ = ['get_basename', 'get_extension', 'directory_contains', 'copy_file', 'move', 'create_tempfile', 'create_tempdir']


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
    foo =>
    include.c => c
    /opt/foo.txt => txt
    foo.bar.h => bar
    /opt//tomcat/webapps/junk.war => war
    .jar => jar
    """
    h,t = os.path.split(fname)
    x = string.split(t, '.')

    if len(x) == 1:
        return ''
    return x[1]


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


def copy_file(src, dst):
    """
    Wrapper for shutil copy methods
    src - file to be copied
    dst - destination file name or directory
    """
    copy2(src, dst)


def copy_tree(src, dst, symlinks=False, ignore=None):
    """
    Wrapper for shutil copytree method
    src - source tree
    dst - destination directory
    symlinks - copy symbolic links
    ignore - do not copy files/directory that matches pattern
    """
    copytree(src, dst, symlinks, ignore)


def move(src, dst):
    shutil.move(src, dst)


def create_tempfile():
    return tempfile.mkstemp()


def create_tempdir():
    return tempfile.mkdtemp()


def test_get_basename(fname):
    print("test_get_basename:", " path:", fname)
    print("result: ", get_basename(fname))


def test_get_extension(fname):
    print("test_get_extension:", " path:", fname)
    print(get_extension(fname))


def test_dir_contains(d, f):
    print("test_dir_contains:", " dir:", d, " file: ", f)
    print("result:", directory_contains(d, f))


if __name__ == "__main__":
    # test_get_basename("foo")
    #test_get_basename("include.c")
    #test_get_basename("/opt/foo.txt")
    #test_get_basename("foo.bar.h")
    #test_get_basename("/opt//tomcat/webapps/junk.war")
    test_get_extension("foo")
    test_get_extension("include.c")
    test_get_extension("/opt/foo.txt")
    test_get_extension("foo.bar.h")
    test_get_extension("/opt//tomcat/webapps/junk.war")
    test_get_extension(".jar")
    test_dir_contains(".", "curl_no_proxy.py")
    test_dir_contains(".", "_proxy.py")
