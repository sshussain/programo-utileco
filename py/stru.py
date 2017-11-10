import re
import string
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
    x = find_files(ignore_case, extension, word, searchpath)
    if count:
        click.echo(len(x))
        click.echo(x.length)
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
    Strip whitespaces at start and end of string. Replace multiple whitespaces with single SPACE
    """
    if not s:
        return s
    origstr = s
    chgstr = re.sub('^\s+', '', origstr)
    chgstr = re.sub('\s+', ' ', chgstr)
    chgstr = re.sub('\s+$', '', chgstr)
    return chgstr

def find_files(ignore_case, extension, word, searchpath):
    return []


if __name__ == '__main__':
    cli()

# vim: tabstop=4 shiftwidth=4 expandtab smartindent
