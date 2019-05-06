def init():
    input_string = input("Enter a string: ")
    count = 0
    upper_string(input_string)
    lower_string(input_string)
    convertion_to_list(input_string)
    reverse(input_string)
    splitting(input_string)

def upper_string(input_string):
    upper = input_string.upper()
    print("String {} is uppered case.".format(upper))

def lower_string(input_string):
    lower = input_string.lower()
    print("String {} is lowered case.".format(lower))

def convertion_to_list(input_string):
    string_list = list(input_string)
    print(string_list)

def reverse(input_string):
    reverse_word = ""
    i = len(input_string)-1
    while(i != -1):
        reverse_word += input_string[i]
        i-=1
    print("The reverse string of {} is {}".format(input_string, reverse_word))

init()