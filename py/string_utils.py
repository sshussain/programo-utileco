import os, sys
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
    # TODO use regex to check string
    return s.isalnum()

if __name__ == "__main__":
    print is_alpha_numeric("123")
    print is_alpha_numeric("junk")
    print is_alpha_numeric("junk12")
    print is_alpha_numeric("$$junk12")
    print is_alpha_numeric("$$junk12%% ^^")

# vim: tabstop=4 shiftwidth=4 expandtab smartindent
