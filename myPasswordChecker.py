#welcome

def program():
    
    print("Welcome to the passowrd checker")
    print("="*50)

    '''
    Input for username
    Asks and saves the user input
    '''

    userName = input("Please enter your user name: ")
    print("="*50)

    '''
    Input for Password
    asks and saves the user input
    '''

    password = ("Bananas123")
    
    tries = 0
    checkPass = ""
    while checkPass != password:
        checkPass = input("Please enter your password again (Current Tries",tries + " ")
        print("="*50)
        if checkPass != password:
            print("This is incorrect please try again.")
            print("="*50)
            tries = tries + 1
        if tries >= 3:
            print("You are out of tries, please enter your user name again")
            break

    if checkPass == password:
        print("Well done, you guessed the password correctly")
        ("="*50)

    else:
        print("="*50)

x = 0
while x == 0:
    program()
        
