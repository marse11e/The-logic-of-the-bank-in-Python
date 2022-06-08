user = {
      'Endless' : {
            'phone' : '+996999052004',
            'name' : 'marselle',
            'balance' : 5000,
            'password' : 'endlesskey'
      },
      'zerotwo' : {
            'phone' : '+996555666777',
            'name' : 'Zerotwo',
            'balance' : 587043,
            'password' : 'zerotwo'
      },
}

mars = None

while True:
      if mars is not None:
            print(f'      Здравствуйте уважаемый клиент {mars}\(>_<)/')
      m = input("""
      1 >>> Зарегистрироваться
      2 >>> Авторизоваться
      3 >>> Перевод баланса
      4 >>> Список пользователей
      5 >>> Информация
      6 >>> Номер телефона   
      7 >>> Выйти

      >>> """)
      if m == '1':
            login = input("Пожалуйста введите логин: >>> ")
            name = input("Пожалуйста введите сваё имя: >>> ")
            phone = input("Пожалуйста введите номер телефона: >>> ")
            password = input("Создайте пароль: >>> ")
            password1 = input("Повторите свой пароль: >>> ")
            while password != password1 or len(password) < 8:
                  password = input('Создайте пароль не меньше 8ми символов: >>> ')
                  password1 = input("Повторите свой пароль: >>> ")
            else:
                  user.update({
                        login : {
                              'name' : name,
                              'phone' : phone,
                              'balance' : 100,
                              'password' : password
                        }
                  })
            print("Вы завершили регистрации успешно \(>_<)/")
            mars = login
      elif m == '2':
            if mars is None:
                  login = input('Введите свой логин: >>> ')
                  password = input('Введение пароль: >>> ')
                  if login in user:
                        if password == user[login]['password']:
                              print('Вы прошли верификацию \(>_<)/')
                              mars = login
                        else:
                              print('Неверный пароль /(-_-)\ >>> ')
                  else:
                        print('Извините мы не нашли такого пользователя /(|_|)/ (Пошёл на хуй) ')
            else:
                  print(f'''     Вы уже авторизованны \(>_<)/ 
                        ''')

      elif m == '3':
            if mars is not None:
                  login_recipient = input('Пожалуйста укажите логин получателя (/>_<)/ >>> ')
                  summa = int(input('Введите сумму перевода \(>_<\) >>> '))
                  if login_recipient in user:
                        if summa <= user[mars]['balance']:
                              user[mars]['balance'] -= summa
                              user[login_recipient]['balance'] += summa
                              print('Перевод успешен \(>_<)/ ')
                        else:
                              print('У вас не достаточно средств для перевода /(|_|)\ ')
                  else:
                        print('Извините мы не нашли этого пользователя  /(|_|)\ ')
            else:
                  print('Далбаеб авторизуется потом переводи сваи деньги (=-=) ')
      elif m == '4':
            print(user)
      elif m == '5':
            if user is not None:
                  print(f'''
      Имя: {user[mars]['name']}
      Логин = {mars}
      Ваш счёт составляет: {user[mars]['balance']}
                        ''')
            else:
                  try:
                        abd = '     Далбаеб авторизуется'
                  except KeyError:
                        print(abd)
                  
      elif m == '7':
            mars = None
            print('Вы вышли из авторизации \(>_<)\ ')
      elif m == '6':
            if mars is not None:
                  print('     Номер телефона: ',user[mars]['phone'])
            else:
                  print('     Далбаеб авторизуется')

# user = {
#       'Sabina' : {
#             'phone' : '+996999052004',
#             'name' : 'Sabina',
#             'balance' : 5000,
#             'password' : 'endlesskey'
#       },
#       'Marselle' : {
#             'phone' : '+996555666777',
#             'name' : 'Marselle',
#             'balance' : 587043,
#             'password' : 'zerotwo'
#       },
# }


# print(user['Marselle']['name'])
# user['Sabina']['age'] = 14
# user['Sabina']['name'] = 'Dora'
# print(user['Sabina'])
# user['Sabina']['balance'] = 99999999999999990

# print(user['Sabina'])
