import program.userSearch
import program.downloadImage
import mainP

def picker(MODE=None):
    if MODE == 'img':
        ret = program.downloadImage.main(RETURN=True)
        retI = ret.items()
        exit = False
        print('Type "help" for a list of commands.')
        while not exit:
            
            try:
                command = (input('\nPICKER > ')).lower()
            except KeyboardInterrupt:
                continue

            if command == 'help':
                print('keys - View the keys')
                print('values - View the values')
                print('r - Retrieve entry in said key and value.')
            
            elif command == 'keys':
                for keys, values in retI:
                    print(keys)
            elif command == 'values':
                for keys, values in retI:
                    print(values)
            elif command == 'r':
                print("EXCLUDE 'post'")
                KEY1 = (input('Key 1 : ')).lower()
                KEY2 = (input("Key 2 (Leave blank if none) : ")).lower()

                if KEY2 == 'n' or len(KEY2) <= 0:
                    output = str(ret['post'][KEY1])
                    try:
                        print(output)
                    except IndexError:
                        print('Artist not specified.')
                else:
                    output = ret['post'][KEY1][KEY2]
                    try:
                        output = output.split(' ')
                    except AttributeError:
                        try:
                            print(output[0] + ", " + output[1])
                        except IndexError:
                            print(output[0])
                        continue

                    opt0 = output[0]
                    try:
                        opt1 = output[1]
                    except IndexError:
                        print(output[0])
                        continue

                    output = f'{opt0}, {opt1}'
                    if str(output) == '[]':
                        print('No artist.')
                    else:
                        print(output)
            elif command == 'q':
                exit = True
        mainP.menu()

    elif MODE == 'usr':
        ret = program.userSearch.main(RETURN=True)
        retI = ret.items()
        exit = False
        print('Type "help" for a list of commands.')
        while not exit:

            try:
                command = (input('\nPICKER > ')).lower()
            except KeyboardInterrupt:
                continue

            if command == 'help':
                print('keys - View the keys')
                print('values - View the values')
                print('r - Retrieve entry in said key and value.')
            
            elif command == 'keys':
                for keys, values in retI:
                    print(keys)
            elif command == 'values':
                for keys, values in retI:
                    print(values)
            elif command == 'r':
                KEY = (input('Key: ')).lower()
                try:
                    print(ret[KEY])
                except KeyError:
                    print('Invalid key!')
            elif command == 'q':
                exit = True
        mainP.menu()
    else:
        print('Something is misconfigured.')
