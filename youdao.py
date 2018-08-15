#!/usr/bin/env python3

import requests
from lxml import html
import sys
import subprocess
import time
try:
    import vlc
except:
    pass

if __name__ == "__main__":
    #######################
    #     Print Logo      #
    #######################
    process = subprocess.Popen(['figlet', 'youdao-dict'], stdout=subprocess.PIPE)
    out, err = process.communicate()
    print(out.decode())

    
    #######################
    #     Parse Text      #
    #######################
    word = sys.argv[1]
    print('='*49)
    print(word)
    print('='*49)

    url = 'https://www.youdao.com/w/{}/#keyfrom=dict2.top'.format(word)
    xpath = '//*[@id="phrsListTab"]//div[@class="trans-container"]/ul/li/text()'

    page = requests.get(url)
    tree = html.fromstring(page.content)
    results = tree.xpath(xpath)

    # Print results
    print('有道翻译：')
    for r in results:
        print(r)

    print('网络释义：')
    results = tree.xpath('//div[@id="tWebTrans"]/div[not(@id)]//div[@class="title"]//span/text()')
    for r in results:
        print(r.strip())
    print('='*49)

    #######################
    #     Play Voice      #
    #######################
    if 'vlc' in sys.modules:
        voice_url = "http://dict.youdao.com/dictvoice?audio={}&type=1" # 英音
        voice_url = "http://dict.youdao.com/dictvoice?audio={}&type=2" # 美音
        voice = vlc.MediaPlayer(voice_url.format(word))
        voice.play()
        # Play for a while then exit main program
        # https://stackoverflow.com/questions/49141463/how-to-wait-until-a-sound-file-ends-in-vlc-in-python-3-6
        time.sleep(0.2)
        duration = voice.get_length() / 1000
        time.sleep(duration)
