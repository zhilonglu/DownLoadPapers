# -*-coding:utf-8-*-
import urllib
import sys
import re
reload(sys)
sys.setdefaultencoding('utf-8')
from bs4 import BeautifulSoup
path = "C:\\Users\\NLSDE\\Desktop\\"
#以下是Python2.x读取ACL 2017年的accept paper

url = "https://chairs-blog.acl2017.org/2017/04/05/accepted-papers-and-demonstrations/"
content = urllib.urlopen(url).read()
soup=BeautifulSoup(content,"html.parser")
r_topic = soup.find_all("h2",attrs={'class':None})
topic = soup.find_all("h3",attrs={'class':None})
paper = soup.find_all("ol",attrs={'class':None})
with open(path+"2017_acceptedPaper_ACL.csv","w") as f:
    idx = 0
    f.write("idx,title,author\n")
    for i in range(len(topic)):
        f.write(str(topic[i].string)+"\n")
        title = paper[i].find_all("li")
        for j in range(len(title)):
            idx += 1
            try:
                paper_name = str(title[j].i.string)
            except:
                paper_name = str(title[j].em.string)
            text = title[j].find_all(text=re.compile("Authors:*"))
            paper_author = str(text[0]).replace("\n","").replace(",","#")
            f.write(str(idx)+","+paper_name+","+paper_author+"\n")
    for i in range(2,len(r_topic)):
        f.write(str(r_topic[i].string)+"\n")
        title = paper[i+len(topic)-2].find_all("li")
        for j in range(len(title)):
            idx += 1
            paper_name = str(title[j].i.string)
            text = title[j].find_all(text=re.compile("Authors:*"))
            paper_author = str(text[0]).replace("\n","").replace(",","#")
            f.write(str(idx)+","+paper_name+","+paper_author+"\n")
