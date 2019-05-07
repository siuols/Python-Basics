def init():
    input_value = 1
    try:
        input_value = int(input("Enter numbers and letters: "))
    except Exception as e:
        value_error(input_value, e)
        exception(input_value, e)
        syntax_error(input_value, e)

    try:  
        num = int(input("\nEnter a number to be divided by 0: "))
        zero_division_error(num)
        name_error(num)
        
    except Exception as e:
        print("please enter a valid number.")

    file_error()
    type_error()


def type_error():
    try:
        value = "test" + 2
    except TypeError as e:
        print ("\nException caught: ", e)

def value_error(input_value, e):
    print("Value Error")
    print("\nException caught: ", e)

def exception(input_value, e):
    print ("\nException is the base class for all exceptions. \nIt knows what specific kind of exception the file is currently handling : ")
    print (e)

def zero_division_error(num):
    try:
        number = num / 0
    except ZeroDivisionError as e:
        print ("\nZeroDivisionError shows when a number is divided by 0")
        print ("Exception caught: ", e)

def syntax_error(input_value, e):
    print("\nComma is missing. Enter numbers separated by comma like this 1, 2")

def file_error():
    try:
        print ("opening sample.txt")
        open("sample.txt")
    except FileNotFoundError as e:
        print ("\nException caught: ", e)

def name_error(num):
    try:
        print ("num = num+test")
        num = num+test
    except NameError as e:
        print ("\nException caught: ", e)
init()