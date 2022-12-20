import json
import hashlib
import os

FILE = 'json_db/users.json'


class RegisterMixin:
    '''Миксин для регистрации'''
    @staticmethod
    def hash_password(password):
        salt = os.urandom(32)
        hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100_000)
        return hashed_password

    @staticmethod
    def _validate_password(password, password2):
        if len(password) < 8:
            raise ValueError('Password is to short, must contain at least 8 characters!')
        if password.isdigit() or password.isalpha():
            raise ValueError('Password must contain digits and characters!')
        if password != password2:
            raise ValueError('Passwords didn\'t match!')

    def register(self, username, password, password2):
        self._validate_password(password, password2)

        with open(FILE, 'r') as file:
            try: 
                data = json.load(file)
                id = data[-1]['id'] + 1
            except (IndexError, ValueError):
                data = []
                id = 1
            is_username_used = any([x['username'] == username for x in data])
        
        with open(FILE, 'w') as file:
            if is_username_used:
                json.dump(data, file)
                raise ValueError('Username is already taken!')
            user = {'id': id, 'username': username, 'password': password}
            data.append(user)
            json.dump(data, file)
            return {'status': 201, 'msg': 'Successfully registered!'}


class LoginMixin:
    '''Миксин для логина'''
    def login(self, username, password):
        with open(FILE, 'r') as file:
            data = json.load(file)
            is_registered = any(x['username'] == username for x in data)
            if not is_registered:
                raise ValueError('Username not found!')
        
        user_data = list(filter(lambda x: x['username'] == username, data))[0]
        if user_data['password'] != password:
            raise Exception('Invalid password!')
        return {'status': 200, 'msg': 'Successfully logged in!', 'user': user_data['username']}


class User(RegisterMixin, LoginMixin):
    pass

obj = User()
# print(obj.register('JohnSnow26', '12345john', '12345john'))
# print(obj.register('SansaStark', 'sansa123', 'sansa123'))
print(obj.login('JohnSnow26', '12345john'))


