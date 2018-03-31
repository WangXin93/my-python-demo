from bs4 import BeautifulSoup
from selenium import webdriver
import json
import re
import time
import contextlib
from tqdm import trange

@contextlib.contextmanager 
def open_chrome_driver(executable_path):
    driver = webdriver.Chrome(executable_path=executable_path)
    yield driver
    driver.close()

def get_lectures(driver):
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    lectures = soup.find_all('li',
                             {'class': re.compile(r'newsx n\d{1,} clearfix')})
    for lecture in lectures:
        yield lecture

def get_info_from_lecture_tag(lecture):
    spans = lecture.find_all('span')
    try:
        title = spans[2].text
    except:
        title = None
    try:
        day = spans[0].text
    except:
        day = None
    try:
        month = spans[1].text
    except:
        month = None
    try:
        href = spans[2].a.attrs['href']
    except:
        href = None
    try:
        speaker = re.findall('主讲人：(\S*)', lecture.text)[0]
    except:
        speaker = None
    try:    
        time = re.findall('时间：(\S*)', lecture.text)[0]
    except:
        time = None
    try:
        place = re.findall('地点：(.*)$', lecture.text)[0]
    except:
        place = None
    return {'title': title,
            'day': day,
            'month': month,
            'href': href,
            'speaker': speaker,
            'time': time,
            'place': place}

def main():
    infos = []

    with open_chrome_driver('./chromedriver') as driver:
        driver = webdriver.Chrome(executable_path='./chromedriver')
        driver.get('http://news.dhu.edu.cn/6410/list.htm')
        for i in trange(47):
            for lecture in get_lectures(driver):
                info = get_info_from_lecture_tag(lecture)
                infos.append(info)
            driver.find_element_by_class_name('next').click()

    print("Start save to json...")
    json.dump(infos, open('lecture_infos.json', 'w'))
    print("Save Done.")

if __name__ == "__main__": 
    main()
