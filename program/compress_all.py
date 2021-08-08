import os
import queue
import zipfile
import secrets
import time
from tqdm import tqdm

zip_q = queue.Queue()

class Compress:
    def __init__(self):
        self.path = os.getcwd() + '/DLs'
    
    def zip_files(self, files):
        zipname = secrets.token_urlsafe(8)
        print(f'Compressing to {zipname}.zip.\nPress CTRL+C to abort.')
        try:
            with zipfile.ZipFile(f'{zipname}.zip', 'w') as _zip:
                for file in tqdm(files):
                    _zip.write(file)
        except KeyboardInterrupt:
            os.remove(f'{zipname}.zip')
            return False
        else:
            print(f'Compressed to {zipname}.zip!')
            return True
    
    def get_files(self):
        for dir in os.listdir('DLs'):
            if any(x == '.' for x in dir):
                pass
            else:
                zip_q.put(dir)
        
        files = []
        while zip_q.qsize() > 0:
            current_dir = zip_q.get()
            for file in os.listdir(f'DLs/{current_dir}'):
                files.append(f'DLs/{current_dir}/{file}')
        
        return files
    
    def run_all(self):
        files = self.get_files()
        start = time.time()
        if self.zip_files(files):
            stop = time.time() - start
            print(f'Compression took {stop/60:.2f} minutes.')
        else:
            print('Compression aborted.')
        input('Press any key to continue.')
    
    def get_path(self):
        return self.path

if __name__ == '__main__':
    print('hi')
else:
    pass
