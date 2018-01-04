import urllib
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageUrl):
    global pages
    html = urllib.request.urlopen("http://en.wikipedia.org"+pageUrl)
    soup = BeautifulSoup(html)
    try:
        print(soup.h1.get_text())
        print(soup.find(id="mw-content-text").findAll("p")[0])
        print(soup.find(id="ca-edit").find("span").find("a").attrs['href'])
    except AttributeError:
        print("页面缺少一些属性，不过不必担心！")

    for link in soup.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # get a new page
                newPage = link.attrs['href']
                print("--------------\n" + newPage)
                pages.add(newPage)
                getLinks(newPage)
getLinks("")

