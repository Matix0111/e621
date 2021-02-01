import requests
import urllib.request
import json
import random
from requests.auth import HTTPBasicAuth
import configparser
import time
import mainP

headers = {'user-agent': 'e621-image-downloader-project (by Matix on e621)'}

config = configparser.ConfigParser()
config.read('info.ini')

e6User = config['AUTH']['e6User']
e6Key = config['AUTH']['e6Key']

def main(RETURN=False):
    exit = False
    print('Enter "-q" as username to quit.')
    while not exit:
        name = input('Username: ')

        if name == '-q':
            exit = True
        else:
            responseRAW = requests.get(f'https://e621.net/users.json?search%5Bname_matches%5D={name}', headers=headers, auth=(f'{e6User}', f'{e6Key}'))
            time.sleep(1)
            responseJSON = responseRAW.json()

            if len(responseJSON[0]) <= 0:
                print('Invalid username/username not found!')
                exit = True
            else:
                userID = responseJSON[0]['id']
                response0 = requests.get(f'https://e621.net/users/{userID}.json', headers=headers, auth=(f'{e6User}', f'{e6Key}'))
                time.sleep(1)
                response0JSON = response0.json()
                if RETURN:
                    return response0JSON
                else:
                    username = response0JSON['name']
                    banned = response0JSON['is_banned']
                    avatarID = response0JSON['avatar_id']

                    print(f'User ID: {userID}')
                    print(f'Username: {username}')
                    print(f'Banned: {banned}')
                    print(f'Avatar ID: {avatarID}')
    mainP.menu()

# if __name__ != '__main__':
#     credCheck()