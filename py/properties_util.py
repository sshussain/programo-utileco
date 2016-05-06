from __future__ import print_function
import os
import sys
from collections import OrderedDict
from ConfigParser import ConfigParser

__all__ = ['load_java_properties', 'create_java_properties',
            'load_ini_properties', 'create_ini_properties']

def parse_property_line(l):
    n,_,v = l.partition('=')
    name = n.strip()
    val = v.strip()
    if val.startswith('\''):
        val = val.strip('\'')
    elif val.startswith('"'):
        val = val.strip('"')
    p = {}
    p[name] = val
    return p


def load_java_properties(fname):
    """
    Read java-like properties from file fname, and load them in a dictionary.
    """
    f = open(fname, 'r')
    #properties = dict()
    properties = OrderedDict()
    for line in f:
        line = line.strip()
        if len(line) > 0 and not line.startswith('#'):
            properties.update(parse_property_line(line))
    return properties


def create_java_properties(propd, destf):
    """
    Create java-like property from dictionary contents, and save them in given file.
    """
    f = open(destf, 'w')
    f.write('#This property file was auto generated. Any changes in this file will be lost!\n')
    for k in propd.keys():
        s = str(k) + '=' + str(propd[k])
        f.write(s + '\n')
    f.close()


def load_ini_properties(fname):
    pass


def create_ini_properties(confp, destf):
    pass


def show_dict(d):
    for k,v in d.items():
        print(k,v)


if __name__ == "__main__":
    srcf = sys.argv[1]
    genf = sys.argv[2]
    p = load_java_properties(srcf)
    create_java_properties(p, genf)
    print('Check gen.properties file')
