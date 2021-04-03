import requests
import urllib.request
from requests.auth import HTTPBasicAuth
import configparser
# import mainP

config = configparser.ConfigParser()
config.read('info.ini')

e6User = config['AUTH']['e6User']
e6Key = config['AUTH']['e6Key']

headers = {'user-agent': f'e6Program (Used by {e6User} on e621)'}

def main(RETURN=False):
    exit = False
    print('Enter "-q" as username to quit.')
    while not exit:
        name = input('Username: ')

        if name == '-q':
            exit = True
        else:
            responseRAW = requests.get(f'https://e621.net/users.json?search%5Bname_matches%5D={name}', headers=headers, auth=(f'{e6User}', f'{e6Key}'))
            responseJSON = responseRAW.json()

            if len(responseJSON[0]) <= 0:
                print('Invalid username/username not found!')
                exit = True
            else:
                userID = responseJSON[0]['id']
                response0 = requests.get(f'https://e621.net/users/{userID}/edit.json', headers=headers, auth=(f'{e6User}', f'{e6Key}'))
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

# if __name__ != '__main__':
#     credCheck()