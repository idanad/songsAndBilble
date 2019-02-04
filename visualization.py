import os, fnmatch
def findfiles (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield os.path.join(root, file)

def parse(infile,outfile):
    fin = open(infile, encoding='windows-1252')
    fout = open(outfile, "w+", encoding='windows-1252')
    for line in fin:

        fout.write(line)
    fin.close()
    fout.close()
    copy(outfile,infile)

def copy(input,out):
    with open(input,encoding='windows-1252') as f:
        lines = f.readlines()
        with open(out, "w",encoding='windows-1252') as f1:
            f1.writelines(lines)

if __name__ == "__main__":
    for textfile in findfiles(r'C:\episodes', '*.htm'):
        parse(textfile,textfile[:-4]+'_'+'.txt')

