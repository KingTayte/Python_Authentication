
# This is a program that prompts the user to register and login

while True:
    option = input("To register enter 1 and to login enter 2: ")
    option = option.strip()

    if option == '1':
        action = ''
        while action != 'Exit':
            name = input("Enter your name: ").strip()
            name = name.capitalize()
            surname = input("Enter your surname: ").strip()
            surname = surname.capitalize()
            username = input("Enter your username: ").strip()
            email = input("Enter your email address: ").strip()
            email = email.lower()
            password = input("Enter a password: ").strip()
            confirm_password = input("Enter your password again").strip()

            while password == confirm_password:
                print("Registration Complete!\n")
                print("Please login: ")
                user_name = input("Enter your username: ")
                user_password = input("Enter your password: ")

                if user_name == username and password == user_password:
                    print("You have successfully logged in")
                    action = input("To exit, enter exit: ").strip()
                    action = action.capitalize()
                else:
                    continue
        print("You have successfully logged out!")
    elif option == '2':
        username = ''
        password = ''
        user_name = input("Enter your username: ")
        user_password = input("Enter your password: ")

        if user_name == username and password == user_password:
            print("You have successfully logged in")
            action = input("To exit, enter exit: ").strip()
            action = action.capitalize()
        else:
            print("User not registered, please register:")
            continue
    else:
        print('Invalid Entry, please select correct option')
        continue
