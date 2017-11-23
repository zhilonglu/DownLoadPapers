# -*-coding:utf-8-*-
import urllib.request
import re
from bs4 import BeautifulSoup
import os
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

path = "E:\\PaperLists\\DM\\KDD\\"

url = "http://www.kdd.org/kdd2017/accepted-papers"
# url = "http://www.KDD.org/KDD2017/program/accepted-papers"
content = urllib.request.urlopen(url).read()
soup = BeautifulSoup(content, "html.parser")
htmls = soup.find_all("p")
if not os.path.exists(path+"KDD2017\\"):
    os.mkdir(path+"KDD2017\\")
count = 0
for i in range(len(htmls)):
    try:
        if str(htmls[i].next.name) == "strong":
            ref = htmls[i].next.next['href']
            name = htmls[i].next.next.text
        else:
            ref = htmls[i].next['href']
            name = str(htmls[i].next.contents[0].text)
        pdf_ref = urllib.request.urlopen(ref).read()
        soup = BeautifulSoup(pdf_ref, "html.parser")
        pdf_url = soup.find_all(href=re.compile("http://dl.acm.org/*"))
        paper_url = pdf_url[0]['href']
        paper = urllib.request.urlopen(paper_url).read()
        soup = BeautifulSoup(paper, "html.parser")
        end_url = soup.find_all("nonscript")
        filename = path + "KDD2017\\2017_KDD_" + name + ".pdf"
        count += 1
        if not os.path.exists(filename):
            f = open(filename, 'wb')
            f.write(paper.read())
            f.close()
            print("%d was done!" % count)
    except:
        continue