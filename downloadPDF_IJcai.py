# -*-coding:utf-8-*-
import urllib.request
from bs4 import BeautifulSoup
import re
import os
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
path = "D:\\PaperLists\\AI\\IJCAI\\"

# url = "http://ijcai-16.org/index.php/accepted-papers#main-track"
url = "http://ijcai-16.org/index.php/welcome/view/accepted_papers"
content = urllib.request.urlopen(url).read()
soup = BeautifulSoup(content, "html.parser")
Body = soup.find_all("li")
if not os.path.exists(path + "IJCAI2016\\"):
    os.mkdir(path + "IJCAI2016\\")
count = 0
with open(path + "IJCAI2016\\" + "2016_acceptedPaper_IJCAI.txt", "w", encoding='utf-8') as f:
    for i in range(len(Body)):
        if str(Body[i].contents[0].name) == 'b':
            try:
                count += 1
                name = str(Body[i].contents[0].text)
                authors = str(Body[i].contents[1].text).replace("&nbsp","").replace(",","#")
                f.write(str(count) + "," + name + "," + authors + "\n")
            except:
                continue
