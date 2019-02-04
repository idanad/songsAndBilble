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
    s = s + '<div id="1" class="tabcontent"><table id="t01"><tr><th>כמות אזכורים</th><th>פרק</th><th>שם הספר</th></tr>'
    for line in fin:
        arr=line.split(' ')
        for i in range (0,len(arr)):
            if i%3==0:
                s=s+'<tr><th>'+str(arr[i])+'</th>'
            elif i%3 == 1:
                s=s+'<th>'+str(arr[i])+'</th>'
            else:
                s=s+'<th>'+str(arr[i])+'</th></tr>'

    fin.close()
    s = s + '</table></div>'
    return s

if __name__ == "__main__":
    s=''
    for textfile in findfiles(r'C:\episodes', '*txt'):
        s=parse(textfile,s)
    fin = open('a1.txt','w')
    fin.write(s)
    fin.close()