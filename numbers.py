from math import sqrt

def init():
    try:
        number_input = int(input("Enter a number: "))
        even_number(number_input)
        prime_number(number_input)
        integer_number(number_input)
        square_root(number_input)
        exponent(number_input)
        complex_number(number_input)

    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

def integer_number(number_input):
    print("Converting integer to string: ", str(int(number_input)))

def float_number(number_input):
    print("Converting integer to float: ", str(float(number_input)))

def complex_number(number_input):
    print("The complex equivalent of {} is {}".format(number_input, complex(number_input)))

def even_number(number_input):
    if(number_input % 2 == 0):
        print("{} is an even number".format(number_input))
    else:
        print("{} is not an even number".format(number_input))

def prime_number(number_input):
    if number_input > 1:
       for i in range(2,number_input):
           if (number_input % i) == 0:
               print("{} is not a prime number".format(number_input))
               print("{} times {} is {}".format(i, number_input//i, number_input))
               break
       else:
           print("{} is a prime number.".format(number_input))
    else:
       print("{} is not a prime number.".format(number_input))

def square_root(number_input):
    try:
        print("The SquareRoot of {} is {}.".format(number_input, (sqrt(number_input))))
    except:
        print("This number doesn't have a SquareRoot.")

def exponent(number_input):
    print("{} powered by itself the result will be : {}.".format(number_input,pow(number_input, number_input)))

init()