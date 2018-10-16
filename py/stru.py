#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os
import mmap
import click


@click.group()
def cli():
    """Command line tool for string operations."""


@cli.command('search', short_help='search for word')
@click.option('--ignore-case', '-ic', is_flag=True, default=False, help='case-sensitive search')
@click.option('--count', is_flag=True, default=False, help='Count number of files that contains this word')
@click.option('--extension', '-e', multiple=True, help='search file with this extension')
@click.argument('word', nargs=1)
@click.argument('searchpath', nargs=1)
def search(ignore_case, count, extension, word, searchpath):
    """Search for given word in files and directories.
       The command will not display file names if count specified.
    """
    x = find_files(word, ignore_case, extension, searchpath)
    if count:
        click.echo(len(x))
    else:
        if x:
            click.echo(('\n').join(x))
        else:
            click.echo('')


@cli.command('replace', short_help='find and replace for word')
@click.option('--ignore-case', '-ic', is_flag=True, default=False, help='case-insensitive search word')
@click.option('--count', is_flag=True, default=False, help='count number of files that contains this word')
@click.option('--extension', '-e', multiple=True, help='search file with this extension')
@click.argument('word')
@click.argument('replacewith', nargs=1)
@click.argument('searchpaths', nargs=1)
def replace(ignore_case, count, extension, word, replacewith, searchpaths):
    """Replace given word in files and directries.
       The command will not display file names if count flag is specified.
    """


def squeeze_ws(s):
    """
    Strip whitespaces at start and end of string. Replace multiple whitespaces
    with single SPACE
    """
    if not s:
        return s
    origstr = s
    chgstr = re.sub('^\s+', '', origstr)
    chgstr = re.sub('\s+', ' ', chgstr)
    chgstr = re.sub('\s+$', '', chgstr)
    return chgstr


def find_files(word, ignore_case, extensions, searchpath):
    allfiles = []
    for root, dirs, files in os.walk(searchpath):
        if not files:
            continue
        for f in files:
            s = '%s/%s' % (root, f)
            if extensions:
                fext = get_extension(f)
                if fext in extensions:
                    if is_word_in_file(s, word):
                        allfiles.append(s)
            else:
                if is_word_in_file(s, word):
                    allfiles.append(s)
    return allfiles


def is_word_in_file(fname, word):
    """ Search word in given file. This function skips empty files.
    """
    f = open(fname)
    try:
        s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        if s.find(word) != -1:
            return True
        return False
    except ValueError:
        pass
    return False


def get_extension(f):
    if not f:
        return None
    _, fext = os.path.splitext(f)
    return fext[1:]


def find_full_word(fname, word):
    pass
# import re
#
# regex = r"\b\w+\b"
#
# test_str = ("jjjk mamm\n"
# 	"hello l;adksd;l 	")
#
# matches = re.finditer(regex, test_str)
#
# for matchNum, match in enumerate(matches):
#     matchNum = matchNum + 1
#
#     print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
#
#     for groupNum in range(0, len(match.groups())):
#         groupNum = groupNum + 1
#
#         print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))


if __name__ == '__main__':
    cli()

# vim: tabstop=4 shiftwidth=4 expandtab smartindent
