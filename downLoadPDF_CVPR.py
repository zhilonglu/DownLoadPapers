# -*-coding:utf-8-*-
import urllib.request
import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
from bs4 import BeautifulSoup

path = "D:\\PaperLists\\AI\\CVPR\\"

url = "https://www.cv-foundation.org/openaccess/CVPR2015.py"
content = urllib.request.urlopen(url).read()
soup = BeautifulSoup(content, "html.parser")
if not os.path.exists(path+"CVPR2015\\"):
    os.mkdir(path+"CVPR2015\\")
details = soup.find_all("dd")
# print(len(author))
#code to write the paper list accepted
# with open(path+"2017_acceptedPaper_CVPR.csv","w") as f:
#     f.write("index,title,author\n")
#     for i in range(len(title)):
#         if i== 22:
#             print(title[i])
#             print(author[i])
#         titleName = str(title[i].string)
#         authorName = str(author[i].string).replace(",","#")
#         f.write(str(i + 1) + "," + titleName + "," + authorName + "\n")
#code to download the pdf file
count = 0
with open(path + "CVPR2015\\2015_acceptedPaper_CVPR.csv","w") as f1:
    for i in range(1,len(details),2):
        try:
            title = str(details[i].contents[3].contents[3].contents[4]).replace("\"", "").replace(":", "").replace("*", "").replace("?",
                                                                                                                           "").replace(
                                "/", "").replace("\ntitle = {","").replace("},","")
            author = str(details[i].contents[3].contents[3].contents[2]).replace(",","#").replace("\nauthor = {","").replace("}#","")
            prefix = "https://www.cv-foundation.org/openaccess/"
            pdf_url = prefix+str(details[i].contents[1]['href'])
            pdf = urllib.request.urlopen(pdf_url)
            filename = path + "CVPR2015\\" + title + ".pdf"
            count += 1
            f1.write(str(count)+","+title+","+author+"\n")
            # if not os.path.exists(filename):
            #     f = open(filename, 'wb')
            #     f.write(pdf.read())
            #     f.close()
            #     print("%d was done!" % count)
        except:
            continue