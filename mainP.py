import subprocess as sp

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

    print('\t Download Image [1]')
    print('\t User Search    [2]')
    print('\t Exit Program   [99]')

    option = input('\nChoice: ')

    if option == '1':
        import program.downloadImage
    elif option == '2':
        import program.userSearch
    elif option == '99':
        pass

if __name__ == '__main__':
    menu()
else:
    pass