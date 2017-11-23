# -*-coding:utf-8-*-
import urllib.request
from bs4 import BeautifulSoup
import re
import os
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
path = "D:\\PaperLists\\"
# 以下是Python3.x读取NIPS 2016年的accept paper

url = "https://nips.cc/Conferences/2016/Schedule?type=Poster"
content = urllib.request.urlopen(url).read()
soup = BeautifulSoup(content, "html.parser")
Body = soup.find_all("div", "maincardBody")
Footer = soup.find_all("div", "maincardFooter")
PDF = soup.find_all(href=re.compile("http://papers.nips.cc/paper/*"))
with open(path + "2016_acceptedPaper_NIPS.csv", "w", encoding='utf-8') as f1:
    f1.write("index,title,author\n")
    for i in range(len(Body)):
        titleName = str(Body[i].string)
        authorName = str(Footer[i].string).replace("&middot;", "_")
        f1.write(str(i + 1) + "," + titleName + "," + authorName + "\n")
for i in range(len(PDF)):
    name = str(Body[i].string).replace("\"", "").replace(":", "").replace("*", "").replace("?", "").replace("/", "")
    pdf_ulr = PDF[i]['href']
    if not os.path.exists(path + "NIPS2016\\"):
        os.mkdir(path + "NIPS2016\\")
    filename = ""
    if not os.path.exists(path + "NIPS2016\\" + name + ".pdf"):
        filename = path + "NIPS2016\\" + name + ".pdf"
    else:
        continue
    try:
        f = open(filename, 'wb')
    except:
        if not os.path.exists(path + "NIPS2016\\" + "%d.pdf" % (i + 1)):
            filename = path + "NIPS2016\\" + "%d.pdf" % (i + 1)
            f = open(filename, 'wb')
        else:
            continue
    pdf = urllib.request.urlopen(pdf_ulr).read()
    soup = BeautifulSoup(pdf, "html.parser")
    paper_url = soup.find_all(href=re.compile(".*.pdf"))
    url_suffix = paper_url[0]['href']
    paper = urllib.request.urlopen("http://papers.nips.cc" + url_suffix)
    f.write(paper.read())
    f.close()
    print("%d was done!" % (i + 1))
