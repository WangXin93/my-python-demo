from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org" + articleUrl)
    soup = BeautifulSoup(html)
    return soup.find("div", {"id":"bodyContent"}).findAll("a",
                     href=re.compile("^(/wiki/)((?!:).)*$"))
links = getLinks("/wiki/Kevin_Bacon")
goon = 'y'
while len(links) > 0 and goon == 'y':
    newArticle = links[random.randint(0, len(links) - 1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)
    goon = input("Another link?([y]/n)") or 'y'


