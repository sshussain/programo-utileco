#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import click
import tarfile


@click.group()
def cli():
    pass


@cli.command()
@click.option('--display', '-D', default='serial', type=click.Choice(['serial', 'tree']), help='valid formats are serial and tree')
@click.option('--skip-empty', '-se', is_flag=True, default=False, help='Do not show empty  directories')
@click.option('--skip-hidden', '-sh', is_flag=True, default=False, help='Do not show hidden directories. Hidden dir name starts with "."')
@click.argument('startpath')
@click.argument('extensions', nargs=-1)
def listfiles(display, skip_empty, skip_hidden, startpath, extensions):
    if display in 'serial':
        filelist = serial_format(startpath, extensions, skip_hidden)
        displaystr = ('\n').join(filelist)
    else:
        displaystr = tree_format(startpath, extensions)
    if displaystr:
        click.secho('%s' % displaystr, fg='green')


@cli.command()
@click.option('--ignore-case', '-ic', is_flag=True, default=False, help='Case insensitive search. Not implemented, yet!')
@click.argument('startpath', type=click.Path(exists=True))
@click.argument('filename')
def findfile(ignore_case, startpath, filename):
    if len(filename) < 3:
        click.echo('Error: File name should at least have 3 characters')
    else:
        x = search_file(startpath, filename)
        if x:
            click.echo(('\n').join(x))


@cli.command()
@click.option('--skip-empty', '-se', is_flag=True, default=False, help='Skip empty directories')
@click.option('--skip-hidden', '-sh', is_flag=True, default=False, help='Skip hidden directories')
@click.option('--compress', '-c', is_flag=True, default=False, help='Compress archive file')
@click.argument('startpath', type=click.Path(exists=True))
@click.argument('dstnfile', type=click.Path())
@click.argument('extensions', nargs=-1)
def archive(skip_empty, skip_hidden, compress, startpath, dstnfile, extensions):
    click.echo(click.format_filename(dstnfile))
    if os.path.exists(dstnfile):
        click.echo('Error: Cannot overrwrite existing destination file {}.'
                   .format(dstnfile))
        return False
    return do_tar(startpath, dstnfile, compress, skip_empty, skip_hidden, extensions)


@cli.command()
@click.option('--force', '-f', is_flag=True, default=False, help='Overwrite files in destination directory')
@click.argument('archivefile', type=click.Path(exists=True))
@click.argument('dstndir', type=click.Path(exists=True))
def extract(force, archivefile, dstndir):
    return do_untar(archivefile, dstndir, force)


def get_extension(f):
    if not f:
        return None
    _, fext = os.path.splitext(f)
    return fext[1:]


def search_file(startpath, pattern, ignore_case=False):
    """ Search for file that matches pattern.
    For now, search for file that starts with pattern"""

    allfiles = []
    for root, dirs, files in os.walk(startpath):
        if not files:
            continue
        for f in files:
            if f.startswith(pattern):
                s = '%s/%s' % (root, f)
                allfiles.append(s)
    return allfiles


def serial_format(startpath, extensions=None, skip_hidden=False, skip_empty=False):

    allfiles = []

    for root, dirs, files in os.walk(startpath):
        if skip_hidden:
            x = root.split('/')[-1]
            if x.startswith('.') and len(x) > 1:
                continue

        if skip_empty:
            if not files:
                continue

        for f in files:
            s = '%s/%s' % (root, f)
            if extensions:
                fext = get_extension(f)
                if fext in extensions:
                    allfiles.append(s)
            else:
                allfiles.append(s)

    return allfiles


def tree_format(startpath, extensions):
    dstr = ''

    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        dstr = dstr + '{}{}/\n'.format(indent, os.path.basename(root))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            _, fext = os.path.splitext(f)
            if len(fext) > 1:
                fext = fext[1:]
            if extensions:
                if fext in extensions:
                    dstr = dstr + '{}{}\n'.format(subindent, f)
            else:
                dstr = dstr + '{}{}\n'.format(subindent, f)
    return dstr


def do_exclude(fname):
    """Exclude empty file -- size 0
    """
    click.echo('fname: %s' % fname)
    click.echo('len: %d' % os.path.getsize(fname))
    if os.path.getsize(fname) == 0:
        return True
    return False


def do_tar(srcdir, dstnfile, compress=False, empty=False, skip_hidden=False, extensions=None):
    if compress:
        ftype = 'w:gz'
        dstnfile = '%s.%s' % (dstnfile, 'tar.gz')
    else:
        ftype = 'w'
        dstnfile = '%s.%s' % (dstnfile, 'tar')

    with tarfile.open(dstnfile, ftype) as tar:
        flist = serial_format(srcdir, extensions=extensions, skip_hidden=skip_hidden)
        for name in flist:
            tar.add(name)
    tar.close()
    return True


def do_untar(srcfile, dstndir, overrwrite=False):
    if not tarfile.is_tarfile(srcfile):
        click.echo('{} is not a tar file'.format(srcfile))
        return False
    tar = tarfile.open(srcfile)
    tar.extractall(path=dstndir)
    tar.close()
    return True


if __name__ == '__main__':
    cli()
