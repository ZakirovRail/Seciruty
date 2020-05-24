import requests

alphabet = '0123456789abcdefghijklmnopqrstuvwxzy'
base = len(alphabet)

i = 0
lenght = 0


while True:
    # i: 10 -> base
    password = ''
    temp = i
    while temp != 0:
        rest = temp % base
        temp = temp // base
        password = alphabet[rest] + password
    # while len(password) < lenght:
    #     password = '0' + password
    password = alphabet[0] * (lenght - len(password)) + password
    print(i, password)
    response = requests.post('http://127.0.0.1:5000/auth',
                             json={'login': 'cat', 'password': '12345'})
    if response.status_code == 200:
        print('Success!')
        break

    if password == alphabet[-1] * lenght:
        lenght += 1
        i = 0
    else:
        i += 1
