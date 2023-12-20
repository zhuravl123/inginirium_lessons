def ask_passord():
    password = input("Введите пароль")
    if password == "пароль":
        print("Пароли совпадают")
    else:
        print("Пароли не совпадают")

ask_passord()