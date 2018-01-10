from crawl_external_links import *
from urllib.request import urlopen
from bs4 import BeautifulSoup

allExtLinks = set()
allIntLinks = set()

def getAllExternalLinks(siteUrl):
    html = urlopen(siteUrl, timeout=50)
    bsObj = BeautifulSoup(html)
    internalLinks = getInternalLinks(bsObj, splitAddress(siteUrl)[0])
    externalLinks = getExternalLinks(bsObj, splitAddress(siteUrl)[0])
    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            print(link)
    for link in internalLinks:
        if link not in allIntLinks:
            print("即将从中获取外链的URL是： " + link)
            allIntLinks.add(link)
            try:
                getAllExternalLinks(link)
            except Exception as e:
                print("Error %s while %s" % (e, link))
                continue

if __name__ == "__main__":
    getAllExternalLinks("http://oreilly.com")

