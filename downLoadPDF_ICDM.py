# -*-coding:utf-8-*-
import urllib.request
from bs4 import BeautifulSoup
import os
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

path = "E:\\PaperLists\\DM\\ICDM\\"

url = "http://www.ucs.louisiana.edu/~sxk6389/Program/ListofAcceptedPapers.html"
content = urllib.request.urlopen(url).read()
soup = BeautifulSoup(content, "html.parser")
htmls = soup.find_all("tr")
if not os.path.exists(path):
    os.mkdir(path)
if not os.path.exists(path + "ICDM2017\\"):
    os.mkdir(path + "ICDM2017\\")
count = 0
with open(path + "ICDM2017\\" + "2017_acceptedPaper_ICDM.txt", "w") as f1:
    for i in range(len(htmls)):
        try:
            name = str(htmls[i].contents[3].contents[0])
            authors = str(htmls[i].contents[3].contents[2].text)
            count += 1
            f1.write(str(count) + "," + name + "," + authors + "\n")
        except:
            continue
