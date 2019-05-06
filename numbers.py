from math import sqrt

def init():
    try:
        number_input = int(input("Enter a number: "))
        even_number(number_input)
        prime_number(number_input)
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

def even_number(number_input):
    if(number_input % 2 == 0):
        print("{} is an even number".format(number_input))
    else:
        print("{} is not an even number".format(number_input))

def prime_number(number_input):
    if number_input > 1:
       for i in range(2,number_input):
           if (number_input % i) == 0:
               print(number_input,"is not a prime number")
               print(i,"times",number_input//i,"is",number_input)
               break
       else:
           print(number_input,"is a prime number")
    else:
       print(number_input,"is not a prime number")

init()