import os, fnmatch
def findfiles (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield os.path.join(root, file)

def parse(infile,outfile):
    for r in range(0,50):
        if r<10:
            r='0'+str(r)
        delete_list = [' <A HREF="t'+str(r)+'.htm">äëåì</A>','äàæðä ìôø÷ æä']
        fin = open(infile, encoding='windows-1252')
        fout = open(outfile, "w+", encoding='windows-1252')
        i=0
        for line in fin:
            for word in delete_list:
                line = line.replace(word, "")
                if line.__contains__(word):
                    line=line.replace(word,"")

            if line.__contains__('<HR>'):
                i=i+1
            if i>2:
                for word in line:
                    line = line.replace(word,"")
            fout.write(line)
        fout.write('</BODY></HTML>')
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

