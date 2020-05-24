simple_logins = ['admin', 'jack', 'cat']


def generate_simple_login(state):
    if state is None:
        state = 0
    if state == len(simple_logins) - 1:
        next_state = None
    else:
        next_state = state + 1
    return simple_logins[state], next_state


with open('../examples/popular_passwords.txt') as f:
    popular_passwords = f.read().split('/n')


def generate_popular_password(state):
    if state is None:
        state = 0
    if state == len(popular_passwords) - 1:
        next_state = None
    else:
        next_state = state + 1
    return popular_passwords[state], next_state


alphabet = '0123456789abcdefghijklmnopqrstuvwxzy'
base = len(alphabet)


def generate_by_brute_force(state):
    if state is None:
        state = [0, 0]
    i, length = state


    password = ''
    temp = i
    while temp != 0:
        rest = temp % base
        temp = temp // base
        password = alphabet[rest] + password
    password = alphabet[0] * (length - len(password)) + password

    if password == alphabet[-1] * length:
        length += 1
        i = 0
    else:
        i += 1
    next_state = [i, length]
    return password, next_state





















