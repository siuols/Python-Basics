import operator

def init():
    num = []
    try:
        num.append(int(input("Enter first number: ")))
        num.append(int(input("Enter second number: ")))
        num.append(int(input("Enter third number: ")))
        num.append(int(input("Enter fourth number: ")))
        print("\nResults\n")
        append(num)
        compare(num)
        sum_list(num)
        multiply_list(num)
        max_num_in_list(num)
        sort_number_list(num)
        remove_duplicate(num)
        search_specific_number(num)
        slicing_list(num)
    except ValueError:
        print("Please enter a number")

def append(num):
    second_number = num[1]
    print("The second number on the list is : {}".format(second_number))


def compare(num):
    num1 = [12,32,5]
    comp = (num > num1) - (num < num1)
    print("comparing 2 list {} and {} : {}".format(num, num1, comp))
def sum_list(num):
    sum_numbers = 0
    for x in num:
        sum_numbers += x
    print("The sum of the list is "+ str(sum_numbers))

def multiply_list(num):
    product = 1
    for x in num:
        product *= x
    print("The product of the list is "+ str(product))

def max_num_in_list(num):
    maximum = num[0]
    for a in num:
        if a > maximum:
            maximum = a
    print("The highest number in the list is: "+ str(maximum))

def sort_number_list(num):
    num.sort()
    print("Sorted in ascending order: "+ str(num))

def remove_duplicate(num):
    dup_items = set()
    uniq_items = []
    for x in num:
        if x not in dup_items:
            uniq_items.append(x)
            dup_items.add(x)
    print(dup_items)

def search_specific_number(num):
    if 2 in num:
        print("Number 2 was found in the list {} using the 'in' operator".format(num))
    else:
        print("Number 2 was not found in the list {} using the 'in' operator".format(num))

def slicing_list(num):
    print("Slicing the list on the second index would look like this : {} ".format(str(num[0:1])))

init()