def init():
    try:
        num1 = int(input("Input first number: "))
        num2 = int(input("Input second number: "))
        addition(num1, num2)
        subtraction(num1, num2)
        multiplication(num1, num2)
        division(num1, num2)
        modulus(num1,num2)
        exponent(num1, num2)
        equal(num1, num2)
        not_equal(num1, num2)
        less_than(num1, num2)
        greater_than(num1, num2)
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

def modulus(num1, num2):
    print("The remainder of {} and {} is: ".format(num1, num2), str(num1 % num2))

def exponent(num1, num2):
    print("The squared of {} and {} is:".format(num1, num2), str(num1 ** num2))

def equal(num1, num2):
    if (num1 == num2):
        print("{} and {} returned to true".format(num1, num2))
    else:
        print("{} and {} returned to false".format(num1, num2))

def not_equal(num1, num2):
    if(num1 != num2):
        print("{} and {} returned to false".format(num1, num2))
    else:
        print("{} and {} returned to true".format(num1, num2))

def less_than(num1, num2):
    if(num1 < num2):
        print("The operator '<' returned true!")
    else:
        print("The operator '<' returned false!")

def greater_than(num1, num2):
    if(num1 > num2):
        print("The operator '>' returned true!")
    else:
        print("The operator '>' returned false!")




init() 