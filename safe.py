# A Substance Safe that Has a Password Input to Unlock the Safe

# In the safe, if a substance is inputted an incrementing timer is starting that provides support for a user based on how long they have abstaiend from a substance

# Creator: Michael Chen
# Date: 10/20/2020

import hashlib
from timer import Timer
from password import old

t = Timer()
t.start()

def options():
    cyan = '\033[96m'
    white = '\033[97m'
    print(cyan + 
    """     
     __       _         _                         __        __      
    / _\_   _| |__  ___| |_ __ _ _ __   ___ ___  / _\ __ _ / _| ___ 
    \ \| | | | '_ \/ __| __/ _` | '_ \ / __/ _ \ \ \ / _` | |_ / _ \\
    _\ \ |_| | |_) \__ \ || (_| | | | | (_|  __/ _\ \ (_| |  _|  __/
    \__/\__,_|_.__/|___/\__\__,_|_| |_|\___\___| \__/\__,_|_|  \___|
                                                                
    """ + white)
    print("1. Input into the safe")
    print("2. Open safe")
    print("3. Change Password")
    print("4. Quit")

    option = int(input("Please input the number of the option: "))

    if option == 1:
        checkPass()
        check()
        options()
    elif option == 2:
        checkPass()
        print("The safe is open, but you can't do anything about it yet!")
        options()
    elif option == 3:
        getPass()
        options()
    elif option == 4:
        print("Goodbye, thank you for using this service.")
        exit()
    else:
        print("Invalid Option")
        options()

def getPass():
    global changePass
    global old
    if old:
        file = open('password.py', 'w+')
        old = ''
        file.write("old = " + "'" + old + "'")
        file.close()
    changePass = str(input("Please input the password you would like to set: "))
    file = open('password.py', 'w+')
    old = encrypt(changePass)
    file.write("old = " + "'" + old + "'")
    file.close()

def encrypt(x):
    password = hashlib.sha256(x.encode() )
    return password.hexdigest()

def checkPass():
    global new
    while True:
        new = str(input("Please input the password to unlock the safe: "))
        if encrypt(new) == old:
            print("Correct Password")
            return True
        else:
            print("Incorrect, Try Again")
            continue


def substance():
    global sub
    print("1. Weed/Marijuana")
    print("2. Alcohol")
    print("3. Nicotine")
    print("4. Cigarettes")
    print("5. Cocaine")
    print("6. Heroin")
    print("7. Other")

    sub = int(input("Please input the number of the substance: "))

    if sub ==1:
        print("You have abstained from weed for: ", '{:.2f}'.format(t.stop()),"seconds")
    if sub == 2:
        print("You have abstained from alcohol for: ", '{:.2f}'.format(t.stop()),"seconds")
    if sub == 3:
        print("You have abstained from nicotine for: ", '{:.2f}'.format(t.stop()),"seconds")
    if sub == 4:
        print("You have abstained from cigarettes for: ", '{:.2f}'.format(t.stop()),"seconds")
    if sub == 5:
        print("You have abstained from cocaine for: ", '{:.2f}'.format(t.stop()),"seconds")
    if sub == 6:
        print("You have abstained from heroin for: ", '{:.2f}'.format(t.stop()),"seconds")
    
    t.start()

def check():
    selection = print("Would you like to input into the safe? Y/N: ")
    if selection == "Y" or "y" or "Yes" or "yes":
        substance()
    else:
        print("Goodbye, thank you for using this service.")
        exit()

def main():
    # print("Encrypted password is: ", encrypt(changePass))
    options()

main()

