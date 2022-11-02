accounts = {}
while True:
    option = input("Wybierz 'zarejestruj' lub 'zaloguj'")
    login = input("Login:  ")
    password = input("Hasło: ")

    if option == "zarejestruj":
        accounts[login] = password
    elif option == "zaloguj":
        if accounts[login] == password:
            print("Zalogowano")
            break
    else:
        print("Błedne dane")
        continue
