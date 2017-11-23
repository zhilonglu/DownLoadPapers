# -*-coding:utf-8-*-
import urllib
from bs4 import BeautifulSoup

path = "C:\\Users\\NLSDE\\Desktop\\"
# 以下是Python2.x读取EMNLP 2017所有accepted paper代码  读取网页时被禁止访问，问题还未解决
rooturl = "http://emnlp2017.net/accepted-papers.html"

content = urllib.urlopen(rooturl).read()
soup = BeautifulSoup(content, "html.parser")
title = soup.find_all("table", "striped")
print(title)
for i in range(len(title)):
    td = title[i].td
    print(td)
    for j in range(len(td)):
        print(td.get_text())
    break
    # with open(path+"2017_acceptedPaper_EMNLP.csv","w") as f:
