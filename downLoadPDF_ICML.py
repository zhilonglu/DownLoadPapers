# -*-coding:utf-8-*-
import urllib.request
import re
from bs4 import BeautifulSoup

path = "C:\\Users\\NLSDE\\Desktop\\ICML2017\\"
# 以下是Python3.x读取ICML 2017所有accepted paper代码

url = "http://proceedings.mlr.press/v70/"
content = urllib.request.urlopen(url).read()
soup = BeautifulSoup(content, "html.parser")
html = soup.find_all(href=re.compile("http://.*17[a-z].pdf"))
title = soup.find_all("p", "title")
cnt = 1
for i in range(65, len(html)):
    try:
        name = str(title[i].string).replace(":", "_").replace(",", "_").replace("?", "")
    except:
        name = str(i)
    pdf_ulr = html[i]['href']
    try:
        f = open(path + name + ".pdf", 'wb')
    except IOError:
        f = open(path + "%d.pdf" % cnt, 'wb')
    pdf = urllib.request.urlopen(pdf_ulr)
    f.write(pdf.read())
    f.close()
    print("%d was done!" % cnt)
    cnt += 1
