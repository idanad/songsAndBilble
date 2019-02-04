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


def parse(file,s,perek,i):
    fin = open(file,errors='ignore')
    perekname=file[12:-4]
    per=perekname.split(' ')
    if not per[0]==perek:
        s=s+perek+' '+ '- '+str(i)+'\n'
        i=0
    for line in fin:
        if line is not '':
            i=i+1
    fin.close()
    ans=[i,s]
    return ans

if __name__ == "__main__":
    s=''
    i=0
    perek='איוב'
    for textfile in findfiles(r'C:\episodes', '*txt'):
        ans=parse(textfile,s,perek[0],i)
        i=ans[0]
        s=ans[1]
        perekname = textfile[12:-4]
        perek=perekname.split(' ')

    fin = open('ab.txt','w')
    fin.write(s)
    fin.close()