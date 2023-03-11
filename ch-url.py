#!/usr/bin/python3
import sys
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

class color():
    yellow = '\033[93m'
    cyan = '\033[96m'
    red = '\033[91m'
    green = '\033[92m'
    end = '\033[0m'
    blue = '\033[94m'
    violet = '\033[95m'

url_list = []

if len(sys.argv) == 2:
    open_file = open(sys.argv[1], 'r')
    read_file = open_file.readlines()
    for i in read_file:
        url_list.append(i.strip())
else:
    print(f'{color.cyan}[+]{color.end} {color.green}Usage: ./gurl.py [Target]{color.end}')
    print(f'{color.cyan}[+]{color.end} {color.green}Example: ./gurl.py urls.txt{color.end}')

def get_request(url):
    try:
        r = requests.get(url, stream=True, allow_redirects=False, timeout=5000)
        # redirect = requests.get(url)
        for a in list(range(10)):
            success = f'20{a}'
            redir = f'30{a}'
            error = f'40{a}'
            server_error = f'50{a}'
            length = r.headers['Content-length']
            type = r.headers['content-Type']
            if str(r.status_code) in success:
                print(f'{url}\t[{color.cyan}{r.status_code}{color.end}]\t[{color.violet}{length}{color.end}]\t[{color.violet}{type}{color.end}]')
            elif str(r.status_code) in redir:
                print(f'{url}\t[{color.yellow}{r.status_code}{color.end}]\t[{color.violet}{length}{color.end}]\t[{color.violet}{type}{color.end}]\t') #--> {color.green}{redirect.url}{color.end}')
            elif str(r.status_code) in error:
                print(f'{url}\t[{color.red}{r.status_code}{color.end}]\t[{color.violet}{length}{color.end}]\t[{color.violet}{type}{color.end}]')
            elif str(r.status_code) in server_error:
                print(f'{url}\t[{color.red}{r.status_code}{color.end}]\t[{color.violet}{length}{color.end}]\t[{color.violet}{type}{color.end}]')
    except requests.exceptions.RequestException as e:
        return e

def runner():
    threads= []
    with ThreadPoolExecutor(max_workers=50) as executor:
        for url in url_list:
            threads.append(executor.submit(get_request, url))
runner()

