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

    print('\t Download Image            [1]')
    print('\t User Search               [2]')
    print('\t Explorer                  [3]')
    print('\t MD5 To Post               [4]')
    print('\t Download All From User    [5]')
    print('\t Exit Program              [99]')

    option = input('\nChoice: ')

    if option == '1':
        from program.downloadImage import main
        main(RETURN=False)
    elif option == '2':
        from program.userSearch import main
        main(RETURN=False)
    elif option == '3':
        picOrUser = (input('Content or User? [C/u] ')).lower()
        if picOrUser == 'u':
            from program.picker import picker
            picker(MODE='usr')
        elif picOrUser == 'c':
            from program.picker import picker
            picker(MODE='img')
    elif option == '4':
        from program.md5_to_post import main
        main()
    elif option == '5':
        import program.dlallfromusr

    elif option == '99':
        print('Thanks for using! Goodbye!')
        pass

if __name__ == '__main__':
    menu()
else:
    pass