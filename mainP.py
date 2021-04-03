import subprocess as sp
from program.downloadImage import dlImage as m1
from program.userSearch import main as m2
from program.picker import picker as m3
from program.md5_to_post import run as m4
from program.dlallfromusr import Program as m5

def menu():
    sp.call('clear')
    print("#########################################")
    print("# ################## ################## #")
    print("# #                # #                # #")
    print("# #    ############# #    ############# #")
    print("# #    #             #    #             #")
    print("# #    #             #    #             #")
    print("# #    #	     #    #             #")
    print("# #    #             #    #             #")
    print("# #    #             #    #             #")
    print("# #    ########      #    ############# #")
    print("# #           #      #                # #")
    print("# #    ########      #    ########    # #")
    print("# #    #             #    #      #    # #")
    print("# #    #             #    #      #    # #")
    print("# #    #             #    #      #    # #")
    print("# #    #             #    #      #    # #")
    print("# #    #             #    #      #    # #")
    print("# #    ############# #    ########    # #")
    print("# #                # #                # #")
    print("# ################## ################## #")
    print("#########################################\n")

    print('OPTIONS:\n')

    print('\t Download Image            [1]')
    print('\t User Search               [2]')
    print('\t Explorer                  [3]')
    print('\t MD5 To Post               [4]')
    print('\t Download All From User    [5]')
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
        m5()
    elif option == '99':
        print('Thanks for using! Goodbye!')

if __name__ == '__main__':
    menu()
else:
    pass