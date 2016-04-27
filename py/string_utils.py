from __future__ import print_function
import os
import sys
import re
import string

def is_blank(s):
    """
    Return True if string is null or is empty (no characters)
    """
    if s is None or len(s) == 0:
        return True
    return False


def is_alpha_numeric(s):
    """
    Return True if string contains only alphabets and numbers
    """
    if is_blank(s) == True:
        return False
    return s.isalnum()


def squeeze_ws(s):
    """
    Strip whitespaces at start and end of string. Replace multiple whitespaces with single SPACE
    """
    origstr = s
    chgstr = re.sub('^\s+', '', origstr)
    chgstr = re.sub('\s+', ' ', chgstr)
    chgstr = re.sub('\s+$', '', chgstr)
    return chgstr


if __name__ == "__main__":
    print is_alpha_numeric("123")
    print is_alpha_numeric("junk")
    print is_alpha_numeric("junk12")
    print is_alpha_numeric("$$junk12")
    print is_alpha_numeric("$$junk12%% ^^")

# vim: tabstop=4 shiftwidth=4 expandtab smartindent
