# -*-coding:utf-8-*-
import urllib.request
import re
from bs4 import BeautifulSoup

path = "C:\\Users\\NLSDE\\Desktop\\ICDE\\"
# 以下是Python3.x读取ICDE 2016所有accepted paper代码

url = "http://icde2016.fi/papers.php"
content = urllib.request.urlopen(url).read()
soup = BeautifulSoup(content, "html.parser")
# html = soup.find_all(href=re.compile("http://.*17[a-z].pdf"))
title = soup.find_all("b", "bold_font_rep")
author = soup.find_all(style="list-style-type:none")
with open(path + "2016_acceptedPaper.csv", "w") as f:
    for i in range(len(title)):
        try:
            titleName = str(title[i].li.string).replace("\n", "").replace("			 ", "")
        except:
            titleName = "None" if title[i].string == None else title[i].string
        try:
            authorName = str(author[i].li.string).replace("\n", "").replace("			 ", "")
        except:
            authorName = "None" if author[i].string == None else author[i].string
        f.write(str(i + 1) + "___" + authorName + "###" + titleName + "\n")
