#!/usr/bin/env python3

import requests
from lxml import html
import sys
import subprocess

if __name__ == "__main__":
    # Print logo
    process = subprocess.Popen(['figlet', 'youdao-dict'], stdout=subprocess.PIPE)
    out, err = process.communicate()
    print(out.decode())

    word = sys.argv[1]
    print('='*79)
    print(word)
    print('='*79)
    url = 'https://www.youdao.com/w/{}/#keyfrom=dict2.top'.format(word)
    xpath = '//*[@id="phrsListTab"]/div[2]//li/text()'

    page = requests.get(url)
    tree = html.fromstring(page.content)
    results = tree.xpath(xpath)

    # Print results
    print('有道翻译：')
    for r in results:
        print(r)

    print('网络释义:')
    results = tree.xpath('//div[@id="tWebTrans"]/div[not(@id)]//div[@class="title"]//span/text()')
    for r in results:
        print(r.strip())
    print('='*79)
