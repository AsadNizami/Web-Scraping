import sys, os
import requests
from collections import deque

# write your code here
arg = sys.argv
directory = arg[1]
os.makedirs(directory, exist_ok=True)


def save(file_name, data):

    page_dir = os.path.join(directory, file_name.split('.')[0])
    print(page_dir)
    print(data)
    with open(page_dir, 'w', encoding='utf-8') as file:
        file.write(data)


def back_url(url):
    return browse(url)


def browse(url):
    return requests.get(url).text


def make_url(url):
    protocol = 'https://'
    return url if url.startswith(protocol) else protocol + url

prev = deque()
while True:
    url = input()
    if url == 'exit':
        break
    if url == 'back':
        bck = back_url(make_url(prev.pop()))
        save(file_name, browse(bck))
        continue
    if '.' not in url:
        print('Incorrect url1')
        continue
    prev.append(url)
    file_name = url.split('.')[0]
    url = make_url(url)
    save(file_name, browse(url))




