# encoding=utf8
import os, fnmatch
import os.path
import sys


from hebrew_numbers import int_to_gematria
import numpy as np

def findfiles (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield os.path.join(root, file)

def copy(input,out):
    with open(input,'rb') as f:
        lines = f.read()
        lines=lines.decode("utf-8")
        lines = lines.encode('utf-8')
        with open(out, "w") as f1:
            f1.write(lines)

def copy1(input,out):
    with open(input,encoding='utf-8') as f:
        lines = f.readlines()
        with open(out, "w", encoding='utf-8') as f1:
            f1.writelines(lines)

if __name__ == "__main__":
    for textfile in findfiles(r'C:\episodes- updated', '(*.htm'):
        copy(textfile,textfile[:-4]+'_'+'.txt')
        copy1(textfile[:-4]+'_'+'.txt',textfile)

