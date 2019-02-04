import os
from bs4 import BeautifulSoup
import requests
import ast


rootdir = 'Lyrics'


def dicta(file_path, result_path):
    not_succeeded = True
    while(not_succeeded):
        try:
            f = open(file_path, encoding="utf8")
            soup = BeautifulSoup(f.read(), 'xml')
            song_text = soup.find_all(name="lg", attrs={"type":"song lyrics"})[0].text
            r = requests.post("http://pasuk.dicta.org.il/api/markpsukim",
                              json={"data": song_text
                                  , "searchQueryResults": "[]"
                                  , "thresh": 0})
            res = r.text.replace("null","None")
            mid_result = ast.literal_eval(ast.literal_eval(res))
            r2 = requests.post("http://pasuk.dicta.org.il/api/parsetogroups?smin=25&smax=10000",
                              json=mid_result)

            final_results = ast.literal_eval(ast.literal_eval(r2.text))
            result_for_file = {}
            result_file = open(result_path, "a+",encoding='utf-8')
            for result in final_results:
                result_for_file["startIChar"] = result["startIChar"]
                result_for_file["endIChar"] = result["endIChar"]
                result_for_file["text"] = BeautifulSoup(result['text'], "lxml").text.replace('\n',' ')
                matches = []
                for match in result["matches"]:
                    matches.append({"text": BeautifulSoup(match['matchedText'], "lxml").text,
                                    "origin": match['verseDispHeb'],
                                    "score": match['score']})
                result_for_file["matches"] = matches
                print(str(result_for_file), file=result_file)
            f.close()
            result_file.close()
            print("Done : " + file_path)
            not_succeeded = False
        except Exception:
            not_succeeded = True
            print(str(Exception))
            print("fucking exception.. wait 2 sec and try again")


def clear_all_results():
    for subdir, dirs, x in os.walk(rootdir):
        for dir in dirs:
            for dir_relative_path, y, the_files in os.walk(rootdir + "/" + dir):
                for file in the_files:
                    if(file.find(".txt") > -1):
                        os.remove(rootdir + "/" + dir + "/" + file)


clear_all_results()


for subdir, dirs, x in os.walk(rootdir):
    for dir in dirs:
        for dir_relative_path, y, the_files in os.walk(rootdir+"/"+dir):
            for file in the_files:
                result_name = file.replace(".xml",".txt")
                dicta(rootdir+"/"+dir+"/"+file, rootdir+"/"+dir+"/"+result_name)
