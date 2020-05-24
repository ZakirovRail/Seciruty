def iteration_by_passwords_then_by_login(login_generator, password_generator, query):
    password_state is None
    while True:
        password, password_state = password_generator(password_state)

        login_state = None
        while True:
            login, login_state = login_generator(login_state)
            print('Try..', login, password)
            if query(login, password):
                print('Success', login, password)
            if login_state is None:
                break
        if password_state is None:
            break


def iteration_by_logins_then_by_limited_passwords(login_generator, password_generator, query):
    limit = 1000
    login, login_state = login_generator(None)
    while login_state is not None:
        login, login_state = login_generator(login_state)
        password, password_state = password_generator(None)
        for i in range(limit):
            if query(login, password):
                print('Success', login, password)
                break
            password, password_state = password_generator(password_state)
            if password_state is None:
                break
        if login_state is None:
            break
