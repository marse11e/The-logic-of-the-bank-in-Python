class User:
    def __init__(self, name, phone, balance, password):
        self.name = name
        self.phone = phone
        self.balance = balance
        self.password = password


class BankSystem:
    def __init__(self):
        self.users = {
            'Endless': User('marselle', '+996999090998', 999999, 'endlesskey'),
            'zerotwo': User('Zerotwo', '+996555666777', 499999, 'zerotwo')
        }
        self.current_user = None

    def register_user(self):
        login = input('Пожалуйста, введите логин: >>> ')
        name = input('Пожалуйста, введите своё имя: >>> ')
        phone = input('Пожалуйста, введите номер телефона: >>> ')
        password = input('Создайте пароль: >>> ')
        password1 = input('Повторите свой пароль: >>> ')

        while password != password1 or len(password) < 8:
            password = input('Создайте пароль не менее 8 символов: >>> ')
            password1 = input('Повторите свой пароль: >>> ')

        user = User(name, phone, 100, password)
        self.users[login] = user

        print('Вы успешно зарегистрированы (>-_-)>')
        self.current_user = login

    def login_user(self):
        login = input('Введите свой логин: >>> ')
        password = input('Введите пароль: >>> ')

        if login in self.users and password == self.users[login].password:
            print('Вы прошли верификацию (>-_-)>')
            self.current_user = login
        else:
            print('Неверный логин или пароль (>-_-)>')

    def transfer_balance(self):
        recipient_login = input('Введите логин получателя (>-_-)> ')
        amount = int(input('Введите сумму перевода (>-_-)> '))

        if recipient_login in self.users:
            if amount <= self.users[self.current_user].balance:
                self.users[self.current_user].balance -= amount
                self.users[recipient_login].balance += amount
                print('Перевод выполнен успешно (>-_-)>')
            else:
                print('У вас недостаточно средств для перевода (>-_-)>')
        else:
            print('Пользователь не найден (>-_-)>')

    def display_user_info(self):
        if self.current_user is not None:
            user = self.users[self.current_user]
            print(f'''
            Имя: {user.name}
            Логин: {self.current_user}
            Баланс: {user.balance}
            ''')
        else:
            print('Сначала авторизуйтесь, чтобы получить информацию (>-_-)>')

    def display_phone_number(self):
        if self.current_user is not None:
            print('Номер телефона:', self.users[self.current_user].phone)
        else:
            print('Сначала авторизуйтесь, чтобы узнать номер телефона (>-_-)>')

    def main(self):
        while True:
            if self.current_user is not None:
                print(f'Здравствуйте, уважаемый клиент {self.users[self.current_user].name} (>-_-)>')

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
                self.register_user()
            elif m == '2':
                if self.current_user is None:
                    self.login_user()
                else:
                    print('Вы уже авторизованы (>-_-)>')
            elif m == '3':
                if self.current_user is not None:
                    self.transfer_balance()
                else:
                    print('Сначала авторизуйтесь, а потом переводите деньги (>-_-)>')
            elif m == '4':
                print(self.users)
            elif m == '5':
                self.display_user_info()
            elif m == '6':
                self.display_phone_number()
            elif m == '7':
                self.current_user = None
                print('Вы вышли из авторизации (>-_-)>')
            else:
                print('Неверный ввод (>-_-)>')


bank_system = BankSystem()
bank_system.main()
