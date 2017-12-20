# -*-coding:utf-8-*-
import urllib.request
from bs4 import BeautifulSoup
import os
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
path = "E:\\PaperLists\\AI\\IJCAI\\"

# url = "http://ijcai-16.org/index.php/accepted-papers#main-track"
url = "http://www.ijcai.org/proceedings/2013/"
content = urllib.request.urlopen(url).read()
soup = BeautifulSoup(content, "html.parser")
title = soup.find_all('p')
# details = soup.find_all('a')
if not os.path.exists(path + "IJCAI2013\\"):
    os.mkdir(path + "IJCAI2013\\")
for i in range(13,len(title)):
    try:
        file_pdf = title[i].contents[0]['href']
        file_title = title[i].contents[0].text.replace("\"", "_").replace(":", "_").replace("*", "_").replace("?","_").replace("/", "_")
        filename = ""
        if not os.path.exists(path + "IJCAI2013\\" + file_title + ".pdf"):
            filename = path + "IJCAI2013\\2013_IJCAI_" + file_title + ".pdf"
        else:
            continue
        f = open(filename, 'wb')
        # pre_url = "http://www.ijcai.org/"
        paper = urllib.request.urlopen(file_pdf)
        f.write(paper.read())
        f.close()
    except:
        # print("%d was not done!" % (i - 5))
        print(str(file_pdf)+" was not done!")
