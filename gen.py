#!/usr/bin/python

import os
from shutil import copyfile
from markdown import markdown

SOURCE = './src'
TARGET = './output'


def mkd(filename):
    with open(filename, 'r') as fd:
        text = fd.read()
        text = text.replace('.md', '.html')
        m = markdown(text)
    outname = filename.replace(SOURCE, TARGET)
    outname = outname.replace('.md', '.html')
    with open(outname, 'w') as fd:
        fd.write(m)

def walker(directory):
    for filename in os.listdir(directory):
        longname = directory + '/' + filename
        outname = longname.replace(SOURCE, TARGET)
        if os.path.isfile(longname):
            if os.path.exists(outname):
                srctime = os.path.getmtime(longname)
                trgtime = os.path.getmtime(outname)
                if trgtime > srctime:
                    continue
            if longname[-3:] == '.md':
                mkd(longname)
            else:
                copyfile(longname, outname)
            print(longname)
        else:
            if not os.path.exists(outname):
                os.makedirs(outname)
            walker(longname)

if __name__ == '__main__':
    walker(SOURCE)
