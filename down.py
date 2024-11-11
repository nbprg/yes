import warnings,sys
from urllib3.exceptions import InsecureRequestWarning

# Suppress only the InsecureRequestWarning from urllib3
warnings.filterwarnings("ignore", category=InsecureRequestWarning)

import requests
import random
#__prox__ = requests.get(url).text.splitlines()
__prox__ = open('proxy.txt','r').read().splitlines()
def prox():
    choice_one = random.choice(__prox__)
    proxy = {
    "http": f"{choice_one}",
    "https": f"{choice_one}"
    }
    return proxy

from concurrent.futures import ThreadPoolExecutor as tred
token = input('Put Authorization Token : ')
mail = input('Put accaunt mail : ')
def __rin__():
    bs=[]
    for x in range(100000):
       bs.append('Absd')
    with tred(max_workers=70) as crack:
       __prox__ = ['a','b','c','d','e','f','g','h']
       for jj in bs:
          crack.submit(main,__prox__,token,mail)
from telegram import Bot
def telegram_message(messages):
    print(messages)
loop = 0
err = 0
def main(__prox__,token,mail):
 global loop,err,token,mail
 try:
  for choice_one in __prox__:
    req_xyz = requests.Session()
    headers = {
    'authority': 'www.aeropres.in',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': f'Berear {token}',
    'content-type': 'application/json',
    'origin': 'chrome-extension://fpdkjdnhkakefebpekbdhillbhonfjjp',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    }
    params = {
    'appid': 'undefined',
    }
    json_data = {
    'username': mail,
    'extensionid': 'fpdkjdnhkakefebpekbdhillbhonfjjp',
    'numberoftabs': 0,
    '_v': '1.0.9',
    }
    response = req_xyz.post('https://www.aeropres.in/chromeapi/dawn/v1/userreward/keepalive', params=params,proxies=prox(),headers=headers,json=json_data,verify=False).text
    err+=1
    if 'success":true' in response:
           loop+=1
           print(f'\033[34mTotal Successful Requests \033[33m_:_ \033[32m{loop} \033[0m/\033[31m Error \033[33m_:_\033[31m {str(int(err) - int(loop))}')
 except Exception as e:
    pass
__rin__()
