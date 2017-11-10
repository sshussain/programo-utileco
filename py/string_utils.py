import os
import sys
import re
import string

__all__ = ['is_blank', 'squeeze_ws']
def is_blank(s):
    """
    Return True if string is null or is empty (no characters)
    """
    if s is None or len(s) == 0:
        return True
    return False


def squeeze_ws(s):
    """
    Strip whitespaces at start and end of string. Replace multiple whitespaces with single SPACE
    """
    if is_blank(s):
        return s
    origstr = s
    chgstr = re.sub('^\s+', '', origstr)
    chgstr = re.sub('\s+', ' ', chgstr)
    chgstr = re.sub('\s+$', '', chgstr)
    return chgstr

# vim: tabstop=4 shiftwidth=4 expandtab smartindent
