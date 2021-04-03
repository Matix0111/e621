import requests
import urllib.request
import json
import random
from requests.auth import HTTPBasicAuth
import configparser
import os
import time
# import mainP

config = configparser.ConfigParser()
config.read('info.ini')

e6User = config['AUTH']['e6User']
e6Key = config['AUTH']['e6Key']

def dlImage(RETURN=False):
    exit = False
    print('Enter "q" as post ID to quit.')
    
    if not RETURN:
        try:
            os.mkdir('DLs/')
        except FileExistsError:
            print('DLs directory already made and found.')

    while not exit:
        post_id = input('Post ID: ')

        if post_id == 'q':
            exit = True
        else:
            headers = {'user-agent': f'e6Program (Used by {e6User} on e621)'}
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