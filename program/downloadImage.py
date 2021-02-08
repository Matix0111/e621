import requests
import urllib.request
import json
import random
from requests.auth import HTTPBasicAuth
import configparser
import os
import time
import mainP

config = configparser.ConfigParser()
config.read('info.ini')

e6User = config['AUTH']['e6User']
e6Key = config['AUTH']['e6Key']

def main(RETURN=False):
    exit = False
    print('Enter "q" as post ID to quit.')

    try:
        os.mkdir('DLs/')
    except FileExistsError:
        print('DLs directory already made and found.')
        while not exit:
            post_id = input('Post ID: ')

            if post_id == 'q':
                exit = True
            else:
                headers = {'user-agent': 'e621-image-downloader-project (by Matix on e621)'}
                responseRAW = requests.get(f'https://e621.net/posts/{post_id}.json', headers=headers, auth=(f'{e6User}', f'{e6Key}'))
                responseJSON = responseRAW.json()

                if RETURN:
                    return responseJSON
                else:
                    url = responseJSON['post']['file']['url']

                    fileExt = url.split('.')
                    fileExt = fileExt[-1]

                    filename = random.randint(1, 10000)
                    full_name = f'DLs/{filename}.{fileExt}'
                    urllib.request.urlretrieve(url, full_name)
                    print('========================')
                    print(f'SUCCESSFULLY SAVED AS {full_name}!')
                    print('========================')

    time.sleep(5)
    mainP.menu()

def credCheck(RETURN=False):
    if e6Key == 'Z' and e6User == 'Z':
        username = input('E6 Username: ')
        api_key = input('E6 API key: ')

        config.get('AUTH', 'e6User')
        config.set('AUTH', 'e6User', username)

        config.get('AUTH', 'e6Key')
        config.set('AUTH', 'e6Key', api_key)
    else:
        main(RETURN=RETURN)