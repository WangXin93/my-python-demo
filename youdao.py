#!/usr/bin/env python3

import requests
from lxml import html
import sys
import subprocess
import time
import urllib
try:
    import vlc
except:
    pass

def translate_word(word):
    print('='*49)
    print(word)
    print('='*49)

    #######################
    #     Parse Text      #
    #######################
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

    play_voice(word)


def translate_sentence(sentence):
    print('='*49)
    print(sentence)
    print('='*49)
    sentence = urllib.parse.quote(sentence)

    #######################
    #     Parse Text      #
    #######################
    url = 'https://www.youdao.com/w/{}/#keyfrom=dict2.top'.format(sentence)
    xpath ='//*[@id="fanyiToggle"]/div/p[2]/text()'

    page = requests.get(url)
    tree = html.fromstring(page.content)
    results = tree.xpath(xpath)

    # Print results
    print('有道翻译：')
    for r in results:
        print(r)

    print('='*49)

    play_voice(sentence)



#######################
#     Play Voice      #
#######################
def play_voice(source, type=2):
    """
    Args:
        source: percent-encoded string
        type: 1 for English, 2 for American
    """
    if 'vlc' in sys.modules:
        voice_url = "http://dict.youdao.com/dictvoice?audio={}&type={}"
        voice = vlc.MediaPlayer(voice_url.format(source, type))
        voice.play()
        # Play for a while then exit main program
        # https://stackoverflow.com/questions/49141463/how-to-wait-until-a-sound-file-ends-in-vlc-in-python-3-6
        time.sleep(0.2)
        duration = voice.get_length() / 1000
        time.sleep(duration)


if __name__ == "__main__":
    #######################
    #     Print Logo      #
    #######################
    process = subprocess.Popen(['figlet', 'youdao-dict'], stdout=subprocess.PIPE)
    out, err = process.communicate()
    print(out.decode())

    original = sys.argv[1:]

    if len(original) == 1:
        translate_word(word)
    elif len(original) > 1:
        translate_sentence(' '.join(original))
