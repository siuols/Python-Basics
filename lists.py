def init():
    num = []
    try:
        num.append(int(input("Enter first number: ")))
        num.append(int(input("Enter second number: ")))
        num.append(int(input("Enter third number: ")))
        num.append(int(input("Enter fourth number: ")))
        print("\nResults\n")
        sum_list(num)
        multiply_list(num)
        max_num_in_list(num)
        sort_number_list(num)
        remove_duplicate(num)
    except ValueError:
        print("Please enter a number")

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

init()