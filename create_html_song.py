import webbrowser
import os, fnmatch
import xml.etree.ElementTree as ET
from hebrew_numbers import gematria_to_int
import codecs
import unicodedata

import json

books = ['', 'בראשית', 'שמות', 'ויקרא', 'במדבר', 'דברים', 'יהושע', 'שופטים', 'שמואל', 'מלכים', 'ישעיהו', 'ירמיהו',
         'יחזקאל', 'הושע', 'יואל', 'עמוס', 'עובדיה', 'יונה', 'מיכה', 'נחום', 'חבקוק', 'צפניה', 'חגי', 'זכריה', 'מלאכי',
         'דברי הימים', 'תהילים', 'איוב', 'משלי', 'רות', 'שיר השירים', 'קהלת', 'איכה', 'אסתר', 'דניאל', 'עזרא/נחמיה']


def findfiles(path, filter):
    # arr=filter.split('|')
    for a in filter:
        for root, dirs, files in os.walk(path):
            for file in fnmatch.filter(files, a):
                yield os.path.join(root, file)


def get_ref_string(matches_index):
    ans_link = ""
    ans = ""
    index_in_loop = 0
    for match2 in matches_index:
        link = match2['origin']
        link_arr = link.split(',')
        link_arr = link_arr[0]
        link_arr = link_arr.split(' ')
        # print(link_arr[0])
        if (link_arr[0] in books):
            index_link = books.index(link_arr[0])
            if (index_link < 10):
                index_link = '0' + str(index_link)
            if (len(link_arr) == 3):
                if (link_arr[1] == 'א'):
                    str_g = gematria_to_int(link_arr[2])
                    if (str_g < 10):
                        str_g = '0' + str(str_g)
                    ans_link = 't' + str(index_link) + 'a' + str(str_g)
                else:
                    str_g = gematria_to_int(link_arr[2]);
                    ans_link = 't' + str(index_link) + 'b' + str(str_g)
            else:
                str_g = gematria_to_int(link_arr[1])
                if (str_g < 10):
                    str_g = '0' + str(str_g)
                ans_link = 't' + str(index_link) + str(str_g)



        else:
            if (link_arr[0] == 'עזרא'):
                str_g = gematria_to_int(link_arr[1])
                if (str_g < 10):
                    str_g = '0' + str(str_g)
                ans_link = 't35a' + str(str_g)
            elif (link_arr[0] == 'נחמיה'):
                str_g = gematria_to_int(link_arr[1])
                if (str_g < 10):
                    str_g = '0' + str(str_g)
                ans_link = 't35b' + str(str_g)
            else:
                index_link = books.index(link_arr[0] + " " + link_arr[1])
                if (index_link < 10):
                    index_link = '0' + str(index_link)
                episode = gematria_to_int(link_arr[2])
                if (episode < 10):
                    episode = '0' + str(episode)
                ans_link = 't' + str(index_link) + str(episode)

        # index_link=books.index(link_arr[0])
        # if(index_link==-1):

        #  print(ans_link)
        if (index_in_loop == 0):
            ans = ans + """                                                <A HREF=""" + "'" + ans_link + """.htm' class="button">                                                         """ + \
                  match2['text'] + " - " + match2[
                      'origin'] + """                                                         </A> """
        else:
            ans = ans + """<br>  <A HREF=""" + "'" + ans_link + """.htm' class="button">                                                                     """ + \
                  match2['text'] + " - " + match2[
                      'origin'] + """                                                                     </A> """
        index_in_loop = index_in_loop + 1;
    ans = ans + """</div> </div> </div>"""

    return ans


def main():
    for textfile in findfiles(r'C:\songs', '*.txt'):

        # print(textfile)
        # print(textfile)
        arr = textfile.split("\\")
        prefix_name = arr[3];
        prefix_name = prefix_name[:-4];
        title_name_new = arr[2] + ' - ' + prefix_name;
        # print(arr)
        # name_song_for_check=arr[3][:-4]
        name1 = arr[2].replace(" ", "")
        name2 = arr[3].replace(" ", "")
        name2 = name2[:-4]
        songname = name1 + '-' + name2

        if (textfile.__contains__('txt')):
            # print(songname);
            file = open(textfile, encoding='utf-8-sig')
            data = file.readlines()

            texts = []
            start_char_arr = []
            end_char_arr = []
            matches = []

            for line in data:
                index = line.find('text');
                index_end = line.find('matches');
                str_replace = line[index - 1:index_end - 1];
                line = line.replace(str_replace, '');
                line = line.replace("\'", "\"");
                # print(line);

                # print(line);
                y = json.loads(line);

                # texts.append(y["text"])
                start_char_arr.append(y["startIChar"])
                end_char_arr.append(y["endIChar"])
                matches.append(y["matches"])

        f = open(songname + '.html', 'a', encoding="utf-8");
        # f.write(message)
        message = """"""

        title_name = ""
        index2 = 0
        len_name = 0
        xml_name = arr[3]
        # print(xml_name)
        message2 = """"""
        if (xml_name.__contains__('xml')):

            # arr2 = textfile.split("\\")
            songname2 = xml_name[:-4]
            # print(songname2)
            # print(songname)
            # print(name_song_for_check)
            # if(songname2==name_song_for_check):
            # print(songname2)
            tree = ET.parse(textfile)
            root = tree.getroot()
            string_data = ""
            string_data_with_line = ""
            for child in root[1][0]:

                for child2 in child:
                    if (index2 == 0):
                        len_name = len(child2.text)
                        title_name = child2.text
                    string_data = string_data + "  "
                    string_data_with_line = string_data_with_line + " \n"
                    for child3 in child2:
                        # print(child3)
                        string_data = string_data + child3.text + " "
                        string_data_with_line = string_data_with_line + child3.text + "\n"
                    index2 = index2 + 1

            normalized = unicodedata.normalize('NFKD', string_data_with_line);
            no_nikkud = ''.join([c for c in normalized if not unicodedata.combining(c)])
            no_nikkud
            string_data_with_line = no_nikkud;
            # print(string_data_with_line);

            # button_one=""
            # indexs=[]
            # last_indexes=[]
            # for text in texts:
            # index=string_data.find(text)
            #  indexs.append(index)
            # last_indexes.append(len(text) + index)
            button_one = ""
            # print(start_char_arr)
            if (len(start_char_arr) > 0):
                if (start_char_arr[0] - len_name + 1 < 0):
                    # print("yes");
                    start_char_arr.pop(0);
                    end_char_arr.pop(0);
                    matches.pop(0);

            if (len(start_char_arr) == 0):
                string_final_ans = string_data_with_line
                # print(string_final_ans)
                # message = """    <em id = "bla" class ="selected-text selected" > """ + message + """<em/> """
            else:
                iter_index = 0
                string_final_ans = ""
                for index in start_char_arr:
                    if (iter_index == 0):
                        string_final_ans = string_final_ans + string_data_with_line[
                                                              :index - len_name + 1] + """<em id="index""" + str(
                            index) + """" class = "selected-text selected">""""" + string_data_with_line[
                                                                                   index - len_name:end_char_arr[
                                                                                                        iter_index] - len_name + 1] + """</em> """;
                        string_final_ans = string_final_ans + """  <div id="popup""" + str(
                            index) + """" style="display: none">                                                   <div id="close""" + str(
                            index) + """" class="modal-content">                                                     <div class="modal-header">                                                       <span id="close-""" + str(
                            index) + """" class="close" inline="display">&times;</span>""" + get_ref_string(
                            matches[iter_index])
                        # <A HREF="t08a01.html" class="button">
                        # """+ str(matches[iter_index])+"""
                        # </A> <br> </div> </div> </div>"""


                    else:
                        string_final_ans = string_final_ans + string_data_with_line[end_char_arr[
                                                                                        iter_index - 1] - len_name + 1:index - len_name + 1] + """<em id="index""" + str(
                            index) + """"   class = "selected-text selected">""" + string_data_with_line[
                                                                                   index - len_name + 1:end_char_arr[
                                                                                                            iter_index] - len_name + 1] + """</em> """
                        string_final_ans = string_final_ans + """  <div id="popup""" + str(
                            index) + """" style="display: none"><div id="close""" + str(
                            index) + """" class="modal-content">                             <div class="modal-header">                               <span id="close-""" + str(
                            index) + """" class="close" inline="display">&times;</span>""" + get_ref_string(
                            matches[iter_index])

                        # <A HREF="t08a01.html" class="button">
                    # בנאי - אבא
                    # </A> <br> </div> </div> </div>"""

                    iter_index = iter_index + 1;
                string_final_ans = string_final_ans + string_data_with_line[
                                                      end_char_arr[iter_index - 1] - len_name + 1:]

            for char in string_final_ans:

                if (char == '\n'):
                    button_one = button_one + "</br>" + char + "</br>"
                else:
                    button_one = button_one + char

            message = """<!DOCTYPE html>
                                          <html>
                                          <LINK REL="stylesheet" HREF="h.css" TYPE="text/css">
                                          <head>
                                                                                                         <div class="topnav">
                                                   <div class="topnav-right">
     <a href=""" + name1 + ".html>" + "לשירים של האמן" + "</a>""""                                         
     <a href="songs_list.html">לרשימת האמנים</a>                                              



    <br></br>
     </div></div> <br></br>

                                           <meta charset="UTF-8">
                                          <center><b><font size="5">""" + title_name_new + """</font></b></center> 

                                          </head>
                                          <body> """
            f.write(message)
            message = ""
            message = message + button_one

            message = """ <center> """ + message + """</center>"""
            # print(message);
            f.write(message)
            message = ""
            for index in start_char_arr:
                message = """<script>
    var p8open = document.getElementById(""" + """'index""""" + str(index) + """'""" + """);
    var p8close = document.getElementById("close-""" + str(index) + """");

    p8open.onclick = function() {
      document.getElementById('popup""" + str(index) + """').style.display = 'block';
    }
    p8close.onclick=function(){
        document.getElementById('popup""" + str(index) + """').style.display = "none";
    }
    </script>"""
                f.write(message)

                message = ""
            message = message + """<br></br>
                          </body>
                          </html>"""

            f.write(message)
            f.close()
            message = ""


if __name__ == "__main__":
    main()




