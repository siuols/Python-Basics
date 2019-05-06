def init():
    try:
        number_input = int(input("Enter a positive number: "))
        if number_input > 0:
            print('\n')
            count_odd_even_numbers(number_input)
            fibonacci(number_input)
            prime_numbers(number_input)
        else:
            print("Please enter a positive number")
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

def count_odd_even_numbers(number_input):
    count_odd = 0
    count_even = 0
    for x in range(number_input):
        if not x % 2:
            count_even+=1
        else:
            count_odd+=1
    print("Number of even numbers :",count_even)
    print("Number of odd numbers :",count_odd)

def fibonacci(number_input):
    list_of_fibonacci = []
    n1 = 0
    n2 = 1
    count = 0
    list_of_fibonacci.append(n1)
    list_of_fibonacci.append(n2)
    catch = number_input - 2
    for counter in range(2, catch+2):
        count = n1 + n2
        n1 = n2
        n2 = count
        list_of_fibonacci.append(count)
    print ("Fibonacci is up until to index '" + str(number_input) + "' are " + str(list_of_fibonacci))

#checks if the number inputted is a prime number
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