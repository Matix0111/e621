import derivehelper
import aeshandler
import os
import getpass
import base64
import hashlib
import configparser

conf = configparser.ConfigParser()

class DownloadDecryptor:
    def __init__(self):
        self.password = getpass.getpass('Password: ').encode()
    
    def derive_key(self):
        k = derivehelper.KDF(self.password, derivehelper.create_salt(self.password))
        return k.derive()
    
    def verify_password(self, aes_inst):
        conf.read('info.ini')
        enc_data = base64.b64decode(conf['ENC_CACHE']['data'].encode())
        decrypted = aes_inst.decrypt(enc_data)
        corr_data = hashlib.sha256(conf['AUTH']['e6User'].encode()).hexdigest()
        try:
            return decrypted.decode() == corr_data
        except UnicodeDecodeError:
            return False
    
    def decrypt_downloads(self, aes_inst, filepaths):
        for file in filepaths:
            with open(file, 'rb') as readfile:
                encrypted_data = readfile.read()
                plain_data = aes_inst.decrypt(encrypted_data)
            
            with open(file, 'wb') as writefile:
                writefile.write(plain_data)
    
    def get_downloads(self):
        filepaths = []
        for _, dirs, files in os.walk('DLs'):
            for _dir in dirs:
                for file in os.listdir(f'DLs/{_dir}'):
                    filepaths.append(f'DLs/{_dir}/{file}')
        
        return filepaths
    
    def start(self):
        master_key = self.derive_key()
        a = aeshandler.AESHandler(master_key, aeshandler.modes.CFB)
        filepaths = self.get_downloads()
        if self.verify_password(a):
            print('Valid. Decrypting files...')
            self.decrypt_downloads(a, filepaths)
        else:
            print('Incorrect password.')

class DownloadEncryptor:
    def __init__(self):
        self.password = getpass.getpass('Password: ').encode()
        self.warning = """
WARNING! Encrypting your downloads results in them being unrecoverable if you forgot your password.
Ensure you store the password away safely, or remember it.
        """
    
    def derive_key(self):
        k = derivehelper.KDF(self.password, derivehelper.create_salt(self.password))
        return k.derive()
    
    def encrypt_downloads(self, aes_inst, filepaths):
        for file in filepaths:
            with open(file, 'rb') as readfile:
                plain_data = readfile.read()
                encrypted_data = aes_inst.encrypt(plain_data)
            
            with open(file, 'wb') as writefile:
                writefile.write(encrypted_data)
    
    def update_ini(self, aes_inst):
        conf.read('info.ini')
        data = hashlib.sha256(conf['AUTH']['e6User'].encode()).hexdigest()
        conf['ENC_CACHE'] = {}
        conf['ENC_CACHE']['data'] = base64.b64encode(aes_inst.encrypt(data)).decode()
        with open('info.ini', 'w') as f:
            conf.write(f)
    
    def get_downloads(self):
        filepaths = []
        for _, dirs, files in os.walk('DLs'):
            for _dir in dirs:
                for file in os.listdir(f'DLs/{_dir}'):
                    filepaths.append(f'DLs/{_dir}/{file}')
        
        return filepaths
    
    def start(self):
        master_key = self.derive_key()
        a = aeshandler.AESHandler(master_key, aeshandler.modes.CFB)
        print('Derived master key...')
        filepaths = self.get_downloads()
        print('Read file paths...')

        print(self.warning)
        proceed = input('Proceed? [Y/n] ').lower()
        if proceed == 'y':
            self.update_ini(a)
            self.encrypt_downloads(a, filepaths)
        else:
            print('Encrypting of downloads aborted.')
