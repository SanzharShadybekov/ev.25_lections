db = {
    'admin': {'username': 'admin', 'password': '1'},
    'hello': {'username': 'hello', 'password': 'hello world'},
}

while True:
    print('Hello, Выберите действия:')
    choice = input('1-register, 2-login, 3-show users: ')
    if choice.strip() == '1':
        print('Pls register new account!')
        username = input('Enter the *username: ')
        password = input('Enter the *password: ')
        password2 = input('Enter the *password cofirmation: ')
        full_name = input('Enter the your full name: ')
        if password != password2:
            print('The password must be match!')
            continue
        elif len(password) < 4:
            print('The invalid password! Too short!')
            continue
        if len(username) < 4:
            print('Invalid username')
            continue
        if full_name:
            db[username] = {'username': username,'password': password, 'full_name': full_name}
            print('Successfully registered!')
        else:
            db[username] = {'username': username, 'password': password}
            print('Successfully registered!')

    elif choice.strip() == '2':
        print('Pls log-in to your account!')
        username = input('Enter your username: ')
        password = input('Enter your password: ')
        try:
            if db[username]['password'] != password:
                print('Invalid password for the account!')
                continue
            try:
                name = db[username]['full_name']
                print(f'Welcome to servis Mr/Mrs {name}!')
            except KeyError:
                name = db[username]['username']
                print(f'Welcome to servis Mr/Mrs {name}!')
        except KeyError:
            print('Account with this username does not exists!')
            continue
    elif choice.strip() == '3':
        for username in db.keys():
            try:
                user = db[username]
                print(f'User: {user["username"]}, Full name: {user["full_name"]}')
            except KeyError:
                print(f'User: {user["username"]}')
    else:
        print('Unsupported operation!')
        continue

    continue_choice = input('Do you want to continue (yes/no)? ')
    if continue_choice.lower().strip() == 'yes':
        continue
    else:
        print('Bye Bye! Good Luck!')
        break
