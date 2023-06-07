def register_user(users):
    login = input('Пожалуйста, введите логин: >>> ')
    name = input('Пожалуйста, введите своё имя: >>> ')
    phone = input('Пожалуйста, введите номер телефона: >>> ')
    password = input('Создайте пароль: >>> ')
    password1 = input('Повторите свой пароль: >>> ')
    
    while password != password1 or len(password) < 8:
        password = input('Создайте пароль не менее 8 символов: >>> ')
        password1 = input('Повторите свой пароль: >>> ')
    
    users[login] = {
        'name': name,
        'phone': phone,
        'balance': 100,
        'password': password
    }
    
    print('Вы успешно зарегистрированы (>-_-)>')
    return login


def login_user(users):
    login = input('Введите свой логин: >>> ')
    password = input('Введите пароль: >>> ')
    
    if login in users and password == users[login]['password']:
        print('Вы прошли верификацию (>-_-)>')
        return login
    else:
        print('Неверный логин или пароль (>-_-)>')
        return None


def transfer_balance(users, current_user):
    recipient_login = input('Введите логин получателя (>-_-)> ')
    amount = int(input('Введите сумму перевода (>-_-)> '))
    
    if recipient_login in users:
        if amount <= users[current_user]['balance']:
            users[current_user]['balance'] -= amount
            users[recipient_login]['balance'] += amount
            print('Перевод выполнен успешно (>-_-)>')
        else:
            print('У вас недостаточно средств для перевода (>-_-)>')
    else:
        print('Пользователь не найден (>-_-)>')


def display_user_info(users, current_user):
    user_info = users[current_user]
    print(f'''
    Имя: {user_info['name']}
    Логин: {current_user}
    Баланс: {user_info['balance']}
    ''')


def display_phone_number(users, current_user):
    if current_user is not None:
        print('Номер телефона:', users[current_user]['phone'])
    else:
        print('Сначала авторизуйтесь, чтобы узнать номер телефона (>-_-)>')


def main():
    users = {
        'Endless': {
            'phone': '+996999090998',
            'name': 'marselle',
            'balance': 999999,
            'password': 'endlesskey'
        },
        'zerotwo': {
            'phone': '+996555666777',
            'name': 'Zerotwo',
            'balance': 499999,
            'password': 'zerotwo'
        }
    }

    mars = None

    while True:
        if mars is not None:
            print(f'Здравствуйте, уважаемый клиент {users[mars]["name"]} (>-_-)>')

        m = input('''
        1 >>> Зарегистрироваться
        2 >>> Авторизоваться
        3 >>> Перевод баланса
        4 >>> Список пользователей
        5 >>> Информация
        6 >>> Номер телефона
        7 >>> Выйти

        >>> ''')

        if m == '1':
            mars = register_user(users)
        elif m == '2':
            if mars is None:
                mars = login_user(users)
            else:
                print('Вы уже авторизованы (>-_-)>')
        elif m == '3':
            if mars is not None:
                transfer_balance(users, mars)
            else:
                print('Сначала авторизуйтесь, а потом переводите деньги (>-_-)>')
        elif m == '4':
            print(users)
        elif m == '5':
            if mars is not None:
                display_user_info(users, mars)
            else:
                print('Сначала авторизуйтесь, чтобы получить информацию (>-_-)>')
        elif m == '6':
            display_phone_number(users, mars)
        elif m == '7':
            mars = None
            print('Вы вышли из авторизации (>-_-)>')
        else:
            print('Неверный ввод (>-_-)>')

if __name__ == '__main__':
    main()
