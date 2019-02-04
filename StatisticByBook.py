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
    x=0
    for line in fin:
        s=s+'<div id="ת" class="tabcontent"><table id="t01"><tr><th>כמות אזכורים</th><th>שם האמן</th> </tr>'
        arr=line.split(' ')
        y=arr[1]
        for i in range (1,len(arr)):
            if not arr[i].isdigit():
                if x==0:
                   s=s+'<tr><th>'
                s=s+' '+str(arr[i])
                x=1
            else:
                s=s+'</th><th>'+str(y)+'</th></tr>'
                x=0
                y=str(arr[i])
        s=s+'</table></div>'

    fin.close()
    return s

if __name__ == "__main__":
    s=''
    for textfile in findfiles(r'C:\episodes', '*txt'):
        s=parse(textfile,s)
    fin = open('a1.txt','w')
    fin.write(s)
    fin.close()