def init():
    balance = 5000
    command = ('Y')
    print('You entered you pin Correctly\n')
    while command not in ('n','NO','no','N'):
        print('Press 1 For Your Balance\n')
        print('Press 2 To Make a Withdrawl\n')
        print('Press 3 To Pay in\n')
        print('Press 4 To Return Card\n')
        option = int(input('What Would you like to choose? :'))
        if option == 1:
            print('Your Balance is ',balance,'\n')
            command = input('Would You you like to go back? [y/n] :')
            if command in ('n','NO','no','N'):
                print('Thank You')
                break
        elif option == 2:
            option = ('y')
            withdrawl = float(input('How Much Would you like to withdraw? [10/20/40/60/80/100] for other option enter 1: '))
            if withdrawl in [10, 20, 40, 60, 80, 100]:
                balance = balance - withdrawl
                print ('\nYour Balance is now s',balance)
                command = input('Would You you like to go back? [y/n] : ')
                if command in ('n','NO','no','N'):
                    print('Thank You')
                    break
            elif withdrawl == 1:
                withdrawl = float(input('Please Enter Desired amount : '))
                balance = balance - withdrawl
                print ('\nYour Balance is now s',balance)

        elif option == 3:
            Pay_in = float(input('How Much Would You Like To Pay In? : '))
            balance = balance + Pay_in
            print ('\nYour Balance is now ',balance)
            command = input('Would You you like to go back? [y/n] : ')
            if command in ('n','NO','no','N'):
                print('Thank You')
                break
        elif option == 4:
            print('Please wait while your card is Returned...\n')
            print('Thank you for you service')
            break
        else:
            print('Please Enter a correct number. \n')
            command = ('y')

def verify_pin(pin):
    if pin == '1234':
        return True
    else:
        return False

def log_in():
    tries = 0
    while tries < 4:
        pin = input('Please Enter Your 4 Digit Pin: ')
        if verify_pin(pin):
            print("Pin accepted!")
            return True
        else:
            print("Invalid pin")
            tries += 1
    print("To many incorrect tries. Could not log in")
    return False

def start_menu():
    print('Welcome to XYZ Bank ATM')
    if log_in():
        init()

start_menu()