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


def parse(file,s):
    fin = open(file,errors='ignore')
    perekname=file[12:-4]
    s=s+perekname+' '+ '- '
    i=0
    for line in fin:
        if line is not '':
            i=i+1
    s=s+str(i)+'\n'
    fin.close()
    return s

if __name__ == "__main__":
    s=''
    for textfile in findfiles(r'C:\episodes', '*txt'):
        print('hi')
        print(textfile)
        s=parse(textfile,s)
    fin = open('aa.txt','w')
    fin.write(s)
    fin.close()