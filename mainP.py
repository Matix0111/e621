import os
import platform
import atexit
import shutil
import argparse
from program.downloadImage import dlImage as m1
from program.userSearch import main as m2
from program.picker import picker as m3
from program.md5_to_post import run as m4
from program.dlallfromusr import Program as m5
from program.compress_all import Compress as m6
from program.encrypt_downloads import DownloadEncryptor, DownloadDecryptor

OS = platform.system()

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--threads', help='# of threads to use. Default is 1.', required=False)
args, *leftover = parser.parse_known_args()

if args.threads is not None:
    if not (args.threads).isdigit():
        print('Number of threads must be a number')
        exit()
    else:
        num_of_threads = int(args.threads)
        if num_of_threads > 5 or num_of_threads < 1:
            print('Out of bounds. # of threads must be between 1-5')
            exit()
else:
    num_of_threads = 1

thread_string = f"[!] "
if num_of_threads > 1:
    thread_string += f"{num_of_threads} THREADS"
else:
    thread_string += 'SINGLE-THREADED'

@atexit.register
def clear_pycache():
    try:
        shutil.rmtree('__pycache__/')
    except FileNotFoundError:
        pass
    finally:
        shutil.rmtree('program/__pycache__')

banner = """
#########################################
# ################## ################## #
# #                # #                # #
# #    ############# #    ############# #
# #    #             #    #             #
# #    #             #    #             #
# #    #             #    #             #
# #    ########      #    ############# #
# #           #      #                # #
# #    ########      #    ########    # #
# #    #             #    #      #    # #
# #    #             #    #      #    # #
# #    #             #    #      #    # #
# #    ############# #    ########    # #
# #                # #                # #
# ################## ################## #
#########################################
"""

def menu():
    _EXIT = False
    while not _EXIT:
        if OS == 'Linux':
            os.system('clear')
        elif OS == 'Windows':
            os.system('cls')

        print(banner)
        print(f'OPTIONS:\t{thread_string}\n')

        print('\t Download Image            [1]')
        print('\t User Search               [2]')
        print('\t Explorer                  [3]')
        print('\t MD5 To Post               [4]')
        print('\t Download All From User    [5]')
        print('\t Compress Downloads        [6]')
        print('\t Encrypt Downloads         [7]')
        print('\t Decrypt Downloads         [8]')
        print('\t Exit Program              [99]')

        option = input('\nChoice: ')

        if option == '1':
            m1(RETURN=False)
        elif option == '2':
            m2(RETURN=False)
        elif option == '3':
            picOrUser = (input('Content or User? [C/u] ')).lower()
            if picOrUser == 'u':
                m3(MODE='usr')
            elif picOrUser == 'c':
                m3(MODE='img')
        elif option == '4':
            m4()
        elif option == '5':
            m5(num_of_threads)
        elif option == '6':
            compress = m6()
            compress.run_all()
        elif option == '7':
            de = DownloadEncryptor()
            de.start()
        elif option == '8':
            de = DownloadDecryptor()
            de.start()
        elif option == '99':
            _EXIT = True
            print('Thanks for using! Goodbye!')
        
        if not _EXIT:
            input('Press enter to continue...')

if __name__ == '__main__':
    menu()
else:
    pass
