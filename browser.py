import sys, os
from collections import deque
nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow
and change shape, and that could be a boon to medicine
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's
 Bad Moon Rising. The world is a very different place than
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

# write your code here
arg = sys.argv
directory = arg[1]
os.makedirs(directory, exist_ok=True)


def save(file_name, data):

    page_dir = os.path.join(directory, file_name.split('.')[0])
    print(data)
    with open(page_dir, 'w') as file:
        file.write(data)

def check(url):
    if url == 'bloomberg.com':
        data = bloomberg_com
    if url == 'nytimes.com':
        data = nytimes_com
    return data


lst = deque()
sites = ['bloomberg.com', 'nytimes.com']
while True:
    url = input()
    if url == 'back':
        if not lst:
            print('No prev page found')
            continue
        lst.pop()
        url = lst.pop()
        save(url, check(url))
        continue
    if url not in ['exit', 'back']:
        lst.append(url)
    if url == 'exit':
        break
    if url not in sites:
        print('Error: Incorrect URL')
        continue
    save(url, check(url))



