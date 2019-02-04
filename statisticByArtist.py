import webbrowser
import os, fnmatch
import xml.etree.ElementTree as ET
import codecs
import unicodedata

import json
names={};




def findfiles(path, filter):
    # arr=filter.split('|')
    for a in filter:
        for root, dirs, files in os.walk(path):
            for file in fnmatch.filter(files, a):
                yield os.path.join(root, file)




def main():
    count_tag = 0;
    songs_for_name = [];
    name_folder_before = "א גרויסע מציאה";
    name_new = "";



    for textfile in findfiles(r'C:\songs', '*.txt'):


        arr = textfile.split("\\")

        name_new=arr[2];
        #print(name_new);
        #print(count_tag);


        if (textfile.__contains__('txt')):
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



            if(name_new==name_folder_before):
                it=0;
                for s_c in start_char_arr:
                    count_tag=count_tag + len(matches[it]);
                    it=it+1;


                #count_tag=count_tag + matches[it].length;

            elif (name_new != name_folder_before):
                names[name_folder_before] = count_tag;
                count_tag=0;
                name_folder_before=name_new;



    f = open('statistic3.html', 'a', encoding="utf-8"); #add table to exist html
    for name in names:
            m='<tr>     <td>'+ str(names[name]) +'</td>     <td>'+ name +'</td>   </tr>'
            f.write(m);
    f.write('</table> </center> </body> </html>')




if __name__ == "__main__":
    main()




