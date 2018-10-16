import inspect
import datetime

__all__ = ['print_inheritance']

def print_inheritance(CLAZZ):
    inhtree = inspect.getmro(CLAZZ)
    revtree = inhtree[::-1]
    spaces = ' '
    for i in revtree:
        s = str(i)
        s = s.lstrip('<').rstrip('>').replace('class', '').replace("'", '').strip()
        print(spaces, s)
        spaces = spaces * 2

def today(human=False):
    now = datetime.datetime.now()
    if not human:
        s = now.strftime('%Y %m %d')
    else:
        s = now.strftime('%b, %a %d, %Y')
    return s

def now(human=False):
    now = datetime.datetime.now()
    if not human:
        s = now.strftime('%H %M %S')
    else:
        s = now.strftime('%H:%M:%S %p')
    return s


if __name__ == '__main__':
    print(today())
    print(today(human=True))
    print(now())
    print(now(human=True))
