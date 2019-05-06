def init():
    try:
        num1 = int(input("Input first number: "))
        num2 = int(input("Input second number: "))
        print("\n")
        addition(num1, num2)
        subtraction(num1, num2)
        multiplication(num1, num2)
        division(num1, num2)
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")


def addition(num1, num2):

    print ("The Sum {} and {} is: ".format(num1,num2), str(num1 + num2))


def subtraction(num1, num2):
    print ("The Diffirence {} and {} is: ".format(num1,num2),str(num1 - num2))


def multiplication(num1, num2):
    print("The Product {} and {} is: ".format(num1,num2), str(num1 - num2))


def division(num1, num2):
    if num2 != 0:
        print ("The Quotient {} and {} is: ".format(num1,num2), str(num1 / num2))
    else:
        print("A number cannot be divided by 0!")

init() 