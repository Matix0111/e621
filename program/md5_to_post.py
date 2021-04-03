import requests
import json
from requests.auth import HTTPBasicAuth
import configparser
# import mainP

config = configparser.ConfigParser()
config.read('info.ini')

e6User = config['AUTH']['e6User']
e6Key = config['AUTH']['e6Key']

def run():
    exit = False
    print('Enter "q" as post ID to quit.')
    while not exit:
        Hash = (input('MD5: ')).lower()

        if Hash == 'q':
            exit = True
        else:
            headers = {'user-agent': f'e6Program (Used by {e6User} on e621)'}
            rq = requests.get(f'https://e621.net/posts.json?tags=md5%3A{Hash}', headers=headers, auth=(f'{e6User}', f'{e6Key}'))
            rqJSON = rq.json()

            try:
                postID = rqJSON['posts'][0]['id']
            except IndexError:
                print('Please re-enter the hash.')
                continue

            print('========================')
            print(f'POST ID: {postID}!')
            print('========================')