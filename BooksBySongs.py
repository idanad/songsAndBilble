import os, fnmatch
from hebrew_numbers import gematria_to_int
def findfiles (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield os.path.join(root, file)

def parse(line,songname,set):
    if line.__contains__('origin'):
        startIndex=line.find('\'origin\': \'')
        endIndex=line.find( '\'score\':')
        index=-(len(line)-endIndex)
        s=line[startIndex:index]
        arr=s.split('\'')
        name=arr[3].split(',')
        filename=name[0]+'.txt'
        pasuk=gematria_to_int(name[1][1:])
        new_line=str(pasuk) + " : " + songname+'\n'
        if not set.__contains__(new_line):
            file = open(filename, 'a')
            file.write(new_line)
            file.close()
            set+=new_line
    return set


if __name__ == "__main__":
    for textfile in findfiles(r'C:\songs', '*.txt'):
        set=""
        arr= textfile.split("\\")
        songname=arr[2]+' - '+arr[3][:-4]
        with open(textfile,encoding="utf8") as infile:
            for line in infile:
                set=parse(line,songname,set)