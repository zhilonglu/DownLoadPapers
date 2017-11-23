# -*-coding:utf-8-*-
import urllib.request
import re
from bs4 import BeautifulSoup
import os

path = "D:\\PaperLists\\AI\\ICLR\\"

# url = "http://www.iclr.cc/doku.php?id=iclr2017:conference_posters"
url = "http://www.iclr.cc/doku.php?id=iclr2015:main"
content = urllib.request.urlopen(url).read()
soup = BeautifulSoup(content, "html.parser")
title_1 = soup.find_all("div", attrs={'class': "table sectionedit16"})
title_2 = soup.find_all("div", attrs={'class': "table sectionedit18"})
title_3 = soup.find_all("div", attrs={'class': "table sectionedit20"})
if not os.path.exists(path + "ICLR2015\\"):
    os.mkdir(path + "ICLR2015\\")
# write the paper name and author into csv while download the pdf
count = 0
with open(path + "ICLR2015\\" + "2015_acceptedPaper_ICLR.csv", "w") as f1:
    for title_index in [title_1, title_2, title_1]:
        title = title_index[0].contents[0].contents
        for i in range(3, len(title), 2):
            try:
                v = title[i].contents[2]
                ref = str(v.contents[1]['href'])
                name = str(v.contents[1].contents[0]).replace("\"", "").replace(":", "").replace("*", "").replace("?",
                                                                                                                   "").replace(
                    "/", "")
                author = str(v.contents[len(v) - 1]).replace(",", "#")
                count += 1
                f1.write(str(count) + "," + name + "," + author + "\n")
                pdf = urllib.request.urlopen(ref).read()
                soup = BeautifulSoup(pdf, "html.parser")
                paper_url = soup.find_all(href=re.compile("/pdf*"))
                url_suffix = paper_url[0]['href']
                paper = urllib.request.urlopen("https://arxiv.org" + url_suffix)
                filename = path + "ICLR2015\\" + name + ".pdf"
                if not os.path.exists(filename):
                    f = open(filename, 'wb')
                    f.write(paper.read())
                    f.close()
                    print("%d was done!" % count)
            except:
                continue
