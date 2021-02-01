import requests
import json
import os
import time
import configparser
import urllib.request
from tqdm import tqdm
from requests.auth import HTTPBasicAuth

config = configparser.ConfigParser()
config.read('info.ini')

IDs = []

class gatherPosts():

    def __init__(self, user, api_key):
        self.user = user
        self.api_key = api_key
        self.artist = ""
        self.pages = 0
        self.IDs = []
        self.tag = ""
        self.headers = {'user-agent': 'testProject (By Matix on e621)'}

    def getIDs(self, pages, tag):
        print('Gathering post IDs')
        for i in tqdm(range(pages)):
            response = requests.get(f'https://e621.net/posts.json?page={i}&tags={tag}', headers=self.headers, auth=(self.user, self.api_key))
            responseJSON = response.json()

            data = responseJSON['posts']

            for i in range(len(data)):
                self.IDs.append(data[i]['id'])
            time.sleep(1)

        print('GATHERED IDs')

    def getMaxPages(self, tag):
        print('Gathering max page')
        for i in range(750):
            response = requests.get(f'https://e621.net/posts.json?page={i}&tags={tag}', headers=self.headers, auth=(self.user, self.api_key))

            if len(response.text) <= 12:
                print('Last page has been reached.')
                break
            else:
                print(f'Found a page!')
                self.pages += 1
                time.sleep(1)

        print(f'MAX PAGE: {self.pages}')
        self.getIDs(self.pages, tag)

    def signin(self):
        self.tag = input('Artist/Tag: ')
        self.getMaxPages(self.tag)

class downloadPosts():

    def __init__(self, user, api_key, IDs, Artist):
        self.user = user
        self.api_key = api_key
        self.IDs = IDs
        self.artist = Artist
        self.tag = tag
        self.headers = {'user-agent': 'testProject (By Matix on e621)'}

    def gatherURLs(self):
        print('Downloading images.')
        num = 0
        os.mkdir(f'DLs/{self.artist}')
        for i in tqdm(range(len(self.IDs))):
            response = requests.get(f'https://e621.net/posts/{self.IDs[i]}.json', headers=self.headers, auth=(self.user, self.api_key))
            responseJSON = response.json()

            data = responseJSON['post']['file']['url']

            url = data

            fileExt = url.split('.')
            fileExt = fileExt[-1]

            filename = f'{self.artist}_{num}'
            full_name = f'DLs/{self.artist}/{filename}.{fileExt}'
            urllib.request.urlretrieve(url, full_name)
            num += 1
            time.sleep(1)

e6User = config['AUTH']['e6User']
e6Key = config['AUTH']['e6Key']

O = gatherPosts(e6User, e6Key)
O.signin()

IDs = O.IDs
tag = O.tag

D = downloadPosts(e6User, e6Key, IDs, tag)
D.gatherURLs()