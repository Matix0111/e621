import os
import queue
import zipfile
import secrets

zip_q = queue.Queue()

class Compress:
    def __init__(self):
        self.path = os.getcwd() + '/DLs'
    
    def zip_files(self, files):
        zipname = secrets.token_urlsafe(8)
        print(f'Compressing to {zipname}.zip.\nPress CTRL+C to abort.')
        try:
            with zipfile.ZipFile(f'{zipname}.zip', 'w') as _zip:
                for file in files:
                    _zip.write(file)
        except KeyboardInterrupt:
            os.remove(f'{zipname}.zip')
        else:
            print(f'Compressed to {zipname}.zip!')
    
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
        self.zip_files(files)
    
    def get_path(self):
        return self.path

if __name__ == '__main__':
    print('hi')
else:
    pass
