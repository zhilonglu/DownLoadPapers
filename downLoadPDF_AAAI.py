# -*-coding:utf-8-*-
import urllib.request
from bs4 import BeautifulSoup
import re
import os
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
path = "D:\\PaperLists\\AI\\AAAI\\"

url = "http://www.aaai.org/Library/AAAI/aaai15contents.php"
content = urllib.request.urlopen(url).read()
soup = BeautifulSoup(content, "html.parser")
Body = soup.find_all("p", "left")
for i in range(len(Body)):
    try:
        title = str(Body[i].find_all('a')[0].string).replace("\"", "").replace(":", "").replace("*", "").replace("?",
                                                                                                                 "").replace(
            "/", "")
        author = str(Body[i].find_all('i')[0].string).replace("\"", "").replace(":", "").replace("*", "").replace("?",
                                                                                                                  "").replace(
            "/", "")
        try:
            paper_ref = str(
                re.findall(r"http://www.aaai.org/ocs/index.php/AAAI/AAAI15/paper/view/\d{4}/\d{4}", str(Body[i]).replace("\n",""))[0])
        except:
            try:
                paper_ref = str(
                    re.findall(r"http://www.aaai.org/ocs/index.php/AAAI/AAAI15/paper/view/\d{4}/\d{5}",
                               str(Body[i]).replace("\n", ""))[0])
            except:
                try:
                    paper_ref = str(
                        re.findall(r"http://www.aaai.org/ocs/index.php/AAAI/AAAI15/paper/view/\d{5}/\d{4}",
                                   str(Body[i]).replace("\n", ""))[0])
                except:
                    try:
                        paper_ref = str(
                            re.findall(r"http://www.aaai.org/ocs/index.php/AAAI/AAAI15/paper/view/\d{5}/\d{5}",
                                       str(Body[i]).replace("\n", ""))[0])
                    except:
                        continue
        pdf_ulr = paper_ref.replace("http", "https").replace("view", "viewFile")
        # pdf_ulr = paper_ref.replace("http","https")
        print(pdf_ulr)
        if not os.path.exists(path + "AAAI2015\\"):
            os.mkdir(path + "AAAI2015\\")
        filename = ""
        if not os.path.exists(path + "AAAI2015\\" + title + ".pdf"):
            filename = path + "AAAI2015\\" + title + ".pdf"
        else:
            continue
        f = open(filename, 'wb')
        # except:
        #     if not os.path.exists(path + "AAAI2015\\" + "%d.pdf" % (i + 1)):
        #         filename = path + "AAAI2015\\" + "%d.pdf" % (i + 1)
        #         f = open(filename, 'wb')
        #     else:
        #         continue
        paper = urllib.request.urlopen(pdf_ulr)
        f.write(paper.read())
        f.close()
        print("%d was done!" % (i + 1))
    except:
        print("there is a error in %d" % (i + 1))
