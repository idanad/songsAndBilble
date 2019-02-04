import webbrowser
import os, fnmatch
import xml.etree.ElementTree as ET
import codecs
import unicodedata

names = {};


def findfiles(path, filter):
    # arr=filter.split('|')
    for a in filter:
        for root, dirs, files in os.walk(path):
            for file in fnmatch.filter(files, a):
                yield os.path.join(root, file)


def main():
    songs_for_name = [];
    name_folder_before = "";
    name_new = "";
    for textfile in findfiles(r'C:\songs', '*.txt'):

        if (textfile.__contains__('txt')):
            arr = textfile.split("\\")
            name_new = arr[2];
            if (name_new != name_folder_before):
                songs_for_name = [];
                prefix_name = arr[3];
                prefix_name = prefix_name[:-4];
                title_name_new = arr[2] + '-' + prefix_name;
                songs_for_name.append(prefix_name);
                names[arr[2]] = songs_for_name;
                name_folder_before = name_new;
            else:
                prefix_name = arr[3];
                prefix_name = prefix_name[:-4];
                title_name_new = arr[2] + '-' + prefix_name;
                songs_for_name.append(prefix_name);
                names[arr[2]] = songs_for_name;
                name_folder_before = name_new;

        # print(arr)
    # print(names);
    create_html();


def create_html():
    f = open('songs_list' + '.html', 'a', encoding="utf-8");
    m = """<!DOCTYPE html>
                                                 <html>
                                                 <LINK REL="stylesheet" HREF="h.css" TYPE="text/css">
                                                 <head>
                                                                                                              <div class="topnav">
                                                   <div class="topnav-right">




    <br></br>
  </div>
</div> <br></br>
                                                  <meta charset="UTF-8">
                                                  <center><b><font size="5">""" + "רשימת אמנים " + """</font></b></center> 


                                                 </head>
                                                 <body> <center>"""
    f.write(m);
    for key in names.keys():
        key_new = key.replace(" ", "");
        m = "<p><a href=" + key_new + ".html class=""\"myButton\">" + key + "</a></p>"
        f.write(m);
    m = "</center></body> </html>"""
    f.write(m);
    f.close();

    str_title = "רשימת שירים - "
    for key in names.keys():
        html_name = key.replace(" ", "");
        f = open(html_name + '.html', 'a', encoding="utf-8");
        m = """<!DOCTYPE html>
                                                 <html>
                                                 <LINK REL="stylesheet" HREF="h.css" TYPE="text/css">
                                                 <head>
                                                                                                 <div class="topnav">
                                                   <div class="topnav-right">
     <a href="songs_list.html">לרשימת האמנים</a>                                              



    <br></br>
  </div>
</div> <br></br>
                                                  <meta charset="UTF-8">
                                                  <center><b><font size="5">""" + str_title + key + """</font></b></center> 


                                                 </head>
                                                 <body> <center>"""
        f.write(m);
        for s in names[key]:
            s_new = s.replace(" ", "");
            m = "<p><a href=" + html_name + '-' + s_new + ".html "+ "class=""\"myButton\">" + s + "</a></p>"
            f.write(m);
        m = "</center></body> </html>"""
        f.write(m);
        f.close();


if __name__ == "__main__":
    main()




