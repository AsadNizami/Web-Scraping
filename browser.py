import sys, os
import requests
from collections import deque
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style

arg = sys.argv
directory = arg[1]
os.makedirs(directory, exist_ok=True)


def save(file_name, data):
    file_name_mod = file_name.split('.')[0].strip('https://')
    page_dir = os.path.join(directory, file_name_mod)
    with open(page_dir, 'w', encoding='utf-8') as file_in:
        # file_in.write(Fore.BLUE + data)
        file_in.write(data)
    with open(page_dir, 'r', encoding='utf-8') as file_out:
        for line in file_out:
            print(line)


def browse(url):
    source_code = requests.get(url)
    soup = BeautifulSoup(source_code.content, 'html.parser')
    for i in range(20):
        if 'script' in str(soup):
            soup.script.decompose()
    # print(soup)
    return soup.get_text()
    print(soup.replace('<script', ''))
    return None


def make_url(url):
    protocol = 'https://'
    return url if url.startswith(protocol) else protocol + url


log_list = deque()
while True:
    url = input()
    if url == 'exit':
        break
    if url == 'back':
        if not log_list:
            print('No page found')
            continue
        log_list.pop()
        last_page = log_list.pop()
        # print(last_page)
        bck = make_url(last_page)
        # print(bck)
        save(file_name, browse(bck))
        continue
    if '.' not in url:
        print('Incorrect url')
        continue
    log_list.append(url)
    # print(log_list)
    file_name = url.split('.')[0]
    url = make_url(url)
    save(file_name, browse(url))