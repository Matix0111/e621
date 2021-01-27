import program.userSearch

def picker(MODE=None):
    if MODE == 'img' and IMAGE != None and VALUES != None and KEYS != None and JSON != None:
        pass
    elif MODE == 'usr':
        ret = program.userSearch.main(RETURN=True)
        retI = ret.items()
        exit = False
        print('Type "help" for a list of commands.')
        while not exit:
            command = (input('PICKER > ')).lower()

            if command == 'help':
                print('keys - View the keys')
                print('values - View the values')
                print('retrieve - Retrieve entry in said key and value.')
            
            elif command == 'keys':
                for keys, values in retI:
                    print(keys)
            elif command == 'values':
                for keys, values in retI:
                    print(values)
            elif command == 'retrieve':
                KEY = (input('Key: ')).lower()
                try:
                    print(ret[KEY])
                except KeyError:
                    print('Invalid key!')
    else:
        print('Something is misconfigured.')
