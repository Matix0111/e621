import requests
import json
import os
import shutil
import time
import logging
import mainP
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
        self.pages = 0
        self.IDs = []
        self.poolID = 0
        self.tag = ""
        self.headers = {'user-agent': 'e6Program (By Matix on e621)'}

    def getIDs(self, pages=None, tag=None, POOLVALUE=False):
        if pages == None and tag == None and POOLVALUE == True:
            response = requests.get(f'https://e621.net/pools/{self.poolID}.json', headers=self.headers, auth=(self.user, self.api_key))
            responseJSON = response.json()

            data1 = responseJSON['post_ids']

            try:
                os.mkdir(f'DLs/pool_{self.poolID}')
            except FileExistsError:
                overwrite = (input('The directory for this user already exists. Overwrite or abort? [O/a] ')).lower()

                if overwrite == 'o':
                    shutil.rmtree(f'DLs/pool_{self.poolID}')
                    os.mkdir(f'DLs/pool_{self.poolID}')
                    fileMade = False
                elif overwrite == 'a':
                    print('Abort.')
                    mainP.menu()

            print('Downloading images.')

            num = 0
            for i in tqdm(range(len(data1))):
                response = requests.get(f'https://e621.net/posts/{data1[i]}.json', headers=self.headers, auth=(self.user, self.api_key))
                responseJSON = response.json()

                data = responseJSON['post']['file']['url']

                url = data

                fileExt = url.split('.')
                fileExt = fileExt[-1]

                filename = f'{num}'
                full_name = f'DLs/pool_{self.poolID}/{filename}.{fileExt}'
                try:
                    urllib.request.urlretrieve(url, full_name)
                except urllib.error.URLError:
                    print('Connection timed out!')
                    
                num += 1
                logging.info(f'Downloaded image {full_name}!')
                time.sleep(1)
            mainP.menu()
        else:

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
        self.tag = input('Artist/Tag (indicate a pool with pool_<post_id> ): ')
        poolIndicator = self.tag[0:4]
        if poolIndicator == 'pool':
            self.poolID = self.tag.split('_')
            self.poolID = self.poolID[1]
            # print(poolID)
            self.getIDs(pages=None, tag=None, POOLVALUE=True)
        else:
            self.getMaxPages(self.tag)

class downloadPosts():

    def __init__(self, user, api_key, IDs, Artist):
        self.user = user
        self.api_key = api_key
        self.IDs = IDs
        self.artist = Artist
        self.tag = tag
        self.headers = {'user-agent': 'e6Program (By Matix on e621)'}

    def gatherURLs(self):
        print('Downloading images.')
        num = 0
        for i in tqdm(range(len(self.IDs))):
            response = requests.get(f'https://e621.net/posts/{self.IDs[i]}.json', headers=self.headers, auth=(self.user, self.api_key))
            responseJSON = response.json()

            data = responseJSON['post']['file']['url']

            url = data

            fileExt = url.split('.')
            fileExt = fileExt[-1]

            filename = f'{self.artist}_{num}'
            full_name = f'DLs/{self.artist}/{filename}.{fileExt}'
            try:
                urllib.request.urlretrieve(url, full_name)
            except urllib.error.URLError:
                print('Connection timed out!')
                
            num += 1
            logging.info(f'Downloaded image {full_name}!')
            time.sleep(1)

e6User = config['AUTH']['e6User']
e6Key = config['AUTH']['e6Key']

O = gatherPosts(e6User, e6Key)
O.signin()

IDs = O.IDs
tag = O.tag

fileMade = False

try:
    os.mkdir(f'DLs/{tag}')
    fileMade = True
except FileExistsError:
    overwrite = (input('The directory for this user already exists. Overwrite or abort? [O/a] ')).lower()

    if overwrite == 'o':
        shutil.rmtree(f'DLs/{tag}')
        os.mkdir(f'DLs/{tag}')
        fileMade = False
    elif overwrite == 'a':
        print('Abort.')
        mainP.menu()

logging.basicConfig(filename=f'DLs/{tag}/{tag}_DL_LOG.log', level=logging.INFO, 
    format='%(asctime)s:DL_IMG:%(message)s')

if fileMade:
    logging.info(f'Directory DLs/{tag} created!')
else:
    logging.info(f'Directory DLs/{tag} overwritten!')

D = downloadPosts(e6User, e6Key, IDs, tag)
D.gatherURLs()