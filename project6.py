# encoding=utf8
import os, fnmatch
import os.path


from hebrew_numbers import int_to_gematria
import numpy as np

def findfiles (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield os.path.join(root, file)



books=['','בראשית','שמות','ויקרא','במדבר','דברים','יהושע','שופטים','שמואל','מלכים','ישעיהו','ירמיהו','יחזקאל','הושע','יואל','עמוס', 'עובדיה', 'יונה', 'מיכה', 'נחום', 'חבקוק', 'צפניה', 'חגי', 'זכריה', 'מלאכי', 'דברי הימים','תהילים','איוב','משלי','רות','שיר השירים','קהלת','איכה','אסתר','דניאל','עזרא/נחמיה']
def parse(infile,outfile):
    needtowrite = 0
    stringtowrite = ''

    dbname=infile[13:-4]
    ot=0
    book_num=int(dbname[:3-len(dbname)])
    if book_num is not 35:
        printas=dbname[2:3-len(dbname)]
        book=books[book_num]
        if dbname[2:3-len(dbname)] is 'a':
            book=book+' א'
            ot =1
        if dbname[2:3-len(dbname)] is 'b':
            book=book+' ב'
            ot=1
    else:
        ot =1
        if dbname[2:3-len(dbname)] is 'a':
            book='עזרא'
        else:
            book='נחמיה'
    perek=int(dbname[2+ot:])
    perek_ot= int_to_gematria(perek,'')
    book=book+' '+perek_ot+'.txt'
    songstable=[]
    linestable=[]
    if os.path.isfile(book):
        perek_file = open(book)
        html=0
        body=0
        for line in perek_file:
            cols=line.split(' : ')
            songstable.append(cols[1][:-1])
            linestable.append(cols[0])
    fin = open(infile,errors='ignore')
    fout = open(outfile, "w+")
    for line in fin:
        if line.__contains__('Windows-1255'):
            line=line.replace('Windows-1255','utf-8')

        if line.__contains__('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">'):
            line='<!DOCTYPE HTML>'
        if line.__contains__('<P>'):
            line=line.replace('<P>','')
        if line.__contains__('</html>')and html==1:
            line=''
        if line.__contains__('</body>') and body==1:
            line=''
        if line.__contains__('</html>'):
            html=1
        if line.__contains__('</body>'):
            html=1

        if needtowrite==1:
            line=line+stringtowrite
            needtowrite=0
            stringtowrite=''
            fout.write(line)
            continue
        if line.__contains__('Copyright'):
            line=''
        if line.__contains__('<A NAME="'):
            if line[10:11-len(line)] is '"':
                pasuk_num=line[9:10-len(line)]
            else:
                pasuk_num=line[9:11-len(line)]
            if pasuk_num not in linestable:
                line='</p><p>'+line
            else:
                lines =  [i for i, x in enumerate(linestable) if x == pasuk_num]

                line=line+'</p><p><em id="pasuk-'+pasuk_num+'" class="selected-text selected">'
                needtowrite=1
                stringtowrite = ' </em><div id="popup'+pasuk_num+'" style="display: none"><div id="close'+pasuk_num+'" class="modal-content"><div class="modal-header"><span id="close-'+pasuk_num+'" class="close" inline="display">&times;</span>'
                for i in lines:
                    song_no_spaces=songstable[i].split(' ')
                    song_link=''
                    for sns in song_no_spaces:
                        song_link=song_link+sns
                    stringtowrite=stringtowrite+'<A HREF="'+song_link+'.html" class="button">'+songstable[i]+'</A><br>'
                stringtowrite=stringtowrite[:-4]+'</div></div></div>'
        fout.write(line)
    endstring='<script>\n'
    for l in linestable:
        endstring = endstring + 'var p'+l+'open = document.getElementById(\'pasuk-'+l+'\');\nvar p'+l+'close = document.getElementById("close-'+l+'");\np'+l+'open.onclick = function() {\ndocument.getElementById(\'popup'+l+'\').style.display = \'block\';\n}\np'+l+'close.onclick=function(){\ndocument.getElementById(\'popup'+l+'\').style.display = "none";\n}\n'
    endstring=endstring+'</script>'
    fout.write(endstring)
    fin.close()
    fout.close()
    copy(outfile,infile)

def copy(input,out):
    with open(input) as f:
        lines = f.read()
        with open(out, "w", encoding='utf-8') as f1:
            f1.write(lines)

if __name__ == "__main__":
    for textfile in findfiles(r'C:\episodes', '*.htm'):
        parse(textfile,textfile[:-4]+'_'+'.txt')

